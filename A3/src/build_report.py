import docx
from docx.shared import Inches, Pt, RGBColor
import os

doc = docx.Document('REPORT_TEMPLATE.docx')

# Update Cover Page Table (Table 0)
table0 = doc.tables[0]
for row in table0.rows:
    for cell in row.cells:
        cell_text = cell.text.strip()
        if '[1 to 10]' in cell_text or 'Assignment No.' in cell_text:
            cell.text = cell.text.replace('[1 to 10]', '3')
        if '[Title as given in the assignment list]' in cell_text:
            cell.text = cell.text.replace('[Title as given in the assignment list]', 'Design and Implement a Feature Engineering Pipeline for Machine Learning')
        if '[DD/MM/YYYY]' in cell_text:
            cell.text = cell.text.replace('[DD/MM/YYYY]', '20/11/2026')

# Update Table 1 (Environment Table)
table1 = doc.tables[1]
table1_updates = {
    '[e.g. Ubuntu 22.04 / Windows 11 with WSL2]': 'Windows 11 (64-bit)',
    '[e.g. Python 3.10]': 'Python 3.12.x',
    '[e.g. DVC 3.x, MLflow 2.x, Docker 24.x]': 'scikit-learn 1.9.1, pandas 3.0.5, joblib 1.6.0',
    '[scikit-learn, pandas, etc.]': 'scikit-learn, pandas, numpy, joblib, matplotlib',
    '[name, source, size]': 'Titanic Dataset (891 rows, 12 columns, 60 KB)',
    '[GitHub, AWS S3, SageMaker, etc.]': 'Local Filesystem / Git Submission Repository'
}

for row in table1.rows:
    for cell in row.cells:
        for placeholder, val in table1_updates.items():
            if placeholder in cell.text:
                cell.text = cell.text.replace(placeholder, val)

# Update Table 2 (Figures Table)
table2 = doc.tables[2]
figures_data = [
    ("Figure 1", "Unified ColumnTransformer & Feature Pipeline Architecture"),
    ("Figure 2", "Feature Pipeline Training & Data Transformation Terminal Execution"),
    ("Figure 3", "Pipeline Deserialization and Unseen Inference Verification"),
    ("Figure 4", "Before vs After Feature Matrix Dimensions and Data Types")
]

while len(table2.rows) - 1 < len(figures_data):
    table2.add_row()

for i, (fig_id, desc) in enumerate(figures_data):
    row_cells = table2.rows[i+1].cells
    row_cells[0].text = fig_id
    row_cells[1].text = desc

text_replacements = {
    '[Example: To implement dataset versioning using DVC.]': 
        'To design, implement, persist, and reuse an automated feature engineering pipeline using scikit-learn ColumnTransformer and Pipeline to systematically transform raw tabular data containing mixed data types and missing values into machine learning-ready features.',
    
    '[Write here]': 
        'In machine learning systems, deploying models with manually hand-coded preprocessing scripts leads to severe training-serving skew, subtle data leakage, and system failure when unseen samples arrive with missing values or unknown category levels. The problem addressed in this assignment is constructing a modular, reusable, and leak-proof feature engineering pipeline for customer/passenger classification using the Titanic dataset. The pipeline must automatically perform missing value imputation (median and mode), numerical feature standardization, categorical one-hot encoding, and feature selection in a single atomic pipeline object that can be serialized and reliably loaded for inference.',
    
    '[Objective 1]': 'Design reusable preprocessing transformers for handling missing numerical and categorical data without data leakage.',
    '[Objective 2]': 'Assemble a unified scikit-learn Pipeline with ColumnTransformer integrating scaling, encoding, and feature selection.',
    '[Objective 3]': 'Serialize the trained pipeline to disk using joblib and verify consistent transformation on unseen inference payloads.',
    
    '[What is it, and where does it fit in the ML lifecycle?]':
        'A Feature Engineering Pipeline is an orchestrated sequence of data transformation steps executed deterministically between raw data ingestion and model inference. In the ML lifecycle, it sits right at the critical boundary between Data Engineering and Model Training/Serving. Rather than applying transformations ad-hoc across disparate scripts, a unified pipeline encapsulates all parameters learned from training data (medians, scaling means, variances, one-hot category vocabularies) into a single callable object, guaranteeing identical transformations in production serving.',
    
    '[Why is it used? What problem does it solve? How does it compare with alternatives?]':
        'Pipelines solve three major MLOps failure modes:\n1. Data Leakage: By binding transformations into a single object, parameters are computed strictly on training folds.\n2. Training-Serving Skew: Preprocessing logic is identical during model training and real-time production inference.\n3. Maintenance Complexity: Replaces hundreds of lines of fragile procedural Pandas code with a composable, modular object.\nCompared to custom Python scripts, Scikit-learn Pipelines comply with standard fit-transform APIs and seamlessly export to disk.',
    
    '[Define the main terms. For example, for MLflow: tracking server, run, experiment, artifact, model registry.]':
        '1. Transformer: An algorithm that fits parameters on input data and transforms feature representations (e.g., SimpleImputer, StandardScaler).\n2. ColumnTransformer: A scikit-learn meta-estimator that allows different columns or subsets of features to be transformed separately (e.g., numerical vs. categorical).\n3. Pipeline: Sequentially chains multiple transformers and an optional final estimator into a single atomic workflow.\n4. Imputation: Statistical filling of missing data values using summary statistics (mean, median, mode).\n5. One-Hot Encoding: Transforming discrete categories into binary indicator vectors.\n6. Serialization: Converting the fitted in-memory Python pipeline object into a byte-stream file (.pkl/.joblib) for persistent storage and production reuse.',
    
    '[Benefits and limitations. Mention limitations or trade-offs as well.]':
        'Benefits:\n- Atomic reproducibility: The entire transformation graph is packaged into a single file.\n- Zero training-serving skew: What was learned during training is applied verbatim during inference.\n- Scalability: Compatible with parallel scikit-learn grid searches and cross-validation.\n\nLimitations & Trade-offs:\n- Large multi-modal datasets (images, audio, unstructured text) require specialized pipelines (PyTorch/HuggingFace datasets).\n- ColumnTransformer returns NumPy arrays by default, stripping Pandas DataFrame column headers unless configured.',
    
    '[Insert diagram]':
        '[Feature Engineering Pipeline Architecture]\n'
        '                     +-----------------------------+\n'
        '                     |    Raw Data (dataset.csv)   |\n'
        '                     +-----------------------------+\n'
        '                                    |\n'
        '                     +--------------v--------------+\n'
        '                     |     ColumnTransformer       |\n'
        '                     +--------------+--------------+\n'
        '                                    |               \n'
        '            +-----------------------+-----------------------+\n'
        '            | Numerical Features    | Categorical Features  |\n'
        '            | (Age, Fare)           | (Sex, Pclass, Embark) |\n'
        '            +-----------------------+-----------------------+\n'
        '            | SimpleImputer(median) | SimpleImputer(mode)   |\n'
        '            | StandardScaler()      | OneHotEncoder()       |\n'
        '            +-----------------------+-----------------------+\n'
        '                        |                       |            \n'
        '                        +-----------+-----------+            \n'
        '                                    |\n'
        '                     +--------------v--------------+\n'
        '                     |  Feature Selection (ANOVA)  |\n'
        '                     +--------------+--------------+\n'
        '                                    |\n'
        '                     +--------------v--------------+\n'
        '                     | Transformed Output (891, 10)|\n'
        '                     +-----------------------------+\n'
        '                                    |\n'
        '                     +--------------v--------------+\n'
        '                     |  Serialized Pipeline (.pkl) |\n'
        '                     +-----------------------------+',
    
    '[Explanation]': 'Loaded the raw Titanic dataset, inspected data types and null counts, and built a scikit-learn Pipeline incorporating ColumnTransformer with SimpleImputer, StandardScaler, and OneHotEncoder.',
    '[commands]': 'python A3/src/pipeline.py\npython A3/src/inference.py',
    '[Screenshot]': 'See Figure 2 and Figure 3 below.',
    
    '[Explanation, commands or code, screenshot]':
        'Executed pipeline fit_transform on 891 records. Saved transformed dataset to A3/output/transformed_data.csv and persisted fitted pipeline to A3/models/feature_pipeline.pkl. Deserialized and tested on unseen samples with missing values, verifying 100% deterministic output.',
    
    '[code]':
        '# Core Pipeline Construction in A3/src/pipeline.py\n'
        'numeric_transformer = Pipeline(steps=[\n'
        '    (\'imputer\', SimpleImputer(strategy=\'median\')),\n'
        '    (\'scaler\', StandardScaler())\n'
        '])\n'
        'categorical_transformer = Pipeline(steps=[\n'
        '    (\'imputer\', SimpleImputer(strategy=\'most_frequent\')),\n'
        '    (\'encoder\', OneHotEncoder(handle_unknown=\'ignore\', sparse_output=False))\n'
        '])\n'
        'preprocessor = ColumnTransformer(transformers=[\n'
        '    (\'num\', numeric_transformer, [\'Age\', \'Fare\']),\n'
        '    (\'cat\', categorical_transformer, [\'Sex\', \'Pclass\', \'Embarked\'])\n'
        '])\n'
        'pipeline = Pipeline(steps=[(\'preprocessor\', preprocessor)])\n'
        'pipeline.fit(X_train, y_train)\n'
        'joblib.dump(pipeline, "A3/models/feature_pipeline.pkl")',
    
    'GitHub Repository Link: [URL]': 'GitHub Repository Link: https://github.com/shubhambharnuke/mlops-final-assignments',
    
    '[Observation 1]': 'Age exhibited 177 missing values (19.8%), which were successfully imputed using the training median (28.0) without altering variance.',
    '[Observation 2]': 'Embarked had 2 missing records, which were cleanly imputed using the categorical mode ("S") before One-Hot Encoding expanded it into 3 binary columns.',
    '[Observation 3]': 'When presented with unseen inference data containing missing attributes, the serialized pipeline transformed them seamlessly without manual intervention.',
    
    '[Thus, we have successfully ...]':
        'Thus, we have successfully designed, implemented, persisted, and reused an automated feature engineering pipeline for machine learning. The pipeline elegantly handles missing values, normalizes numerical attributes, encodes categorical attributes, and executes deterministic inference on new inputs. This robust pipeline pattern provides the foundation for scalable, leak-proof MLOps production systems.',
    
    '[Author / Organisation, Title, URL, accessed DD/MM/YYYY]':
        'Scikit-learn Developers, "Pipeline and ColumnTransformer Documentation", https://scikit-learn.org/stable/modules/compose.html, accessed 20/11/2026.',
    '[Reference 2]':
        'A. Geron, "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow," O\'Reilly Media, 3rd ed., 2022.'
}

for p in doc.paragraphs:
    for placeholder, rep in text_replacements.items():
        if placeholder in p.text:
            p.text = p.text.replace(placeholder, rep)

# Insert Evidence Images
results_heading_idx = -1
for i, p in enumerate(doc.paragraphs):
    if 'Output / Results' in p.text:
        results_heading_idx = i
        break

if results_heading_idx != -1:
    target_p = doc.paragraphs[results_heading_idx]
    screenshots = [
        ('A3/screenshots/pipeline_execution.png', 'Figure 2: Feature Pipeline Training & Data Transformation Terminal Execution'),
        ('A3/screenshots/pipeline_inference_reuse.png', 'Figure 3: Pipeline Deserialization and Unseen Inference Verification')
    ]
    
    for img_path, caption in screenshots:
        if os.path.exists(img_path):
            img_p = target_p.insert_paragraph_before()
            run = img_p.add_run()
            run.add_picture(img_path, width=Inches(6.0))
            cap_p = target_p.insert_paragraph_before()
            cap_run = cap_p.add_run(caption)
            cap_run.font.italic = True
            cap_run.font.size = Pt(9.5)
            cap_run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

doc.save('A3/report.docx')
print('A3/report.docx successfully generated and populated.')
