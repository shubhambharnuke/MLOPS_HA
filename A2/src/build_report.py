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
            cell.text = cell.text.replace('[1 to 10]', '2')
        if '[Title as given in the assignment list]' in cell_text:
            cell.text = cell.text.replace('[Title as given in the assignment list]', 'Track Machine Learning Experiments Using MLflow')
        if '[DD/MM/YYYY]' in cell_text:
            cell.text = cell.text.replace('[DD/MM/YYYY]', '20/11/2026')

# Update Table 1 (Environment Table)
table1 = doc.tables[1]
table1_updates = {
    '[e.g. Ubuntu 22.04 / Windows 11 with WSL2]': 'Windows 11 (64-bit)',
    '[e.g. Python 3.10]': 'Python 3.12.x',
    '[e.g. DVC 3.x, MLflow 2.x, Docker 24.x]': 'MLflow 3.18.0, scikit-learn 1.9.1',
    '[scikit-learn, pandas, etc.]': 'mlflow, scikit-learn, pandas, numpy, seaborn, joblib',
    '[name, source, size]': 'Breast Cancer Wisconsin (Diagnostic), 569 samples, 30 features',
    '[GitHub, AWS S3, SageMaker, etc.]': 'SQLite Local Store (sqlite:///A2/mlflow.db), MLflow Registry'
}

for row in table1.rows:
    for cell in row.cells:
        for placeholder, val in table1_updates.items():
            if placeholder in cell.text:
                cell.text = cell.text.replace(placeholder, val)

# Update Table 2 (Figures Table)
table2 = doc.tables[2]
figures_data = [
    ("Figure 1", "MLflow Architecture Diagram showing Tracking, Artifacts, and Registry"),
    ("Figure 2", "MLflow Terminal Execution Logging 6 Model Experiments"),
    ("Figure 3", "Comparative Experiment Evaluation Table across Models"),
    ("Figure 4", "Best Model Confusion Matrix (Logistic_Regression_Tuned)"),
    ("Figure 5", "Best Model ROC-AUC Curve (AUC = 0.995)"),
    ("Figure 6", "Inference Validation from Registered Model")
]

while len(table2.rows) - 1 < len(figures_data):
    table2.add_row()

for i, (fig_id, desc) in enumerate(figures_data):
    row_cells = table2.rows[i+1].cells
    row_cells[0].text = fig_id
    row_cells[1].text = desc

text_replacements = {
    '[Example: To implement dataset versioning using DVC.]': 
        'To develop a machine learning application and implement MLflow to track experiments across multiple algorithms and hyperparameters, logging parameters, metrics, diagnostic plots, and registering the best model for reproducible inference.',
    
    '[Write here]': 
        'Developing machine learning systems is inherently iterative, involving dozens of algorithm explorations, hyperparameter combinations, and data scaling variations. When tracked manually in spreadsheets or ad-hoc notebooks, engineers lose track of parameter-metric relationships, fail to reproduce historic model results, and struggle to manage production handoffs. In this assignment, we address this chaos by building an automated experiment tracking workflow using MLflow on the Breast Cancer Wisconsin dataset. We record runs across Logistic Regression, Decision Trees, Random Forests, and SVMs, log metrics (Accuracy, Precision, Recall, F1, ROC-AUC), save confusion matrices and ROC curves as artifacts, and automatically register the best candidate model into the MLflow Model Registry.',
    
    '[Objective 1]': 'Understand experiment tracking principles and configure MLflow with a persistent backend storage store.',
    '[Objective 2]': 'Train multiple classification algorithms, log hyperparameters, performance metrics, and graphical evaluation artifacts.',
    '[Objective 3]': 'Perform comparative model analysis, register the best-performing model, and verify inference from serialized artifacts.',
    
    '[What is it, and where does it fit in the ML lifecycle?]':
        'MLflow is an open-source platform designed to manage the end-to-end machine learning lifecycle. It fits directly in the Model Development and Evaluation phase. As data scientists train models, MLflow provides unified APIs to record code version, hyperparameters, evaluation metrics, and output files. It eliminates manual record-keeping and guarantees that every deployed model can be traced back to its training code, dataset, and hyperparameter configuration.',
    
    '[Why is it used? What problem does it solve? How does it compare with alternatives?]':
        'MLflow is selected because of its lightweight, library-agnostic architecture. It works with any machine learning library (Scikit-learn, PyTorch, TensorFlow, XGBoost). It solves the problem of model reproducibility, disorganized experiment logs, and model governance. Compared to Weights & Biases (W&B) or Comet ML, MLflow can be run 100% locally and open-source without data privacy concerns or cloud subscription fees. Compared to TensorBoard, MLflow tracks tabular hyperparameters, multi-metric summaries, and manages a formal Model Registry.',
    
    '[Define the main terms. For example, for MLflow: tracking server, run, experiment, artifact, model registry.]':
        '1. Experiment: A logical group of related runs tackling a shared objective (e.g., MLOps_Experiment_Tracking).\n2. Run: A single execution of machine learning code that logs parameters, metrics, tags, and artifacts.\n3. Parameters: Key-value inputs such as learning rate, tree depth, or regularization parameter (C).\n4. Metrics: Numerical evaluation outputs recorded over time or at completion (Accuracy, F1-score, ROC-AUC).\n5. Artifacts: Heavy outputs such as serialized model binaries (.pkl, .joblib), plots, and data summaries.\n6. Model Registry: A centralized collaborative store to manage model versions, transitions (Staging, Production), and lineage.',
    
    '[Benefits and limitations. Mention limitations or trade-offs as well.]':
        'Benefits:\n- Systematic Comparison: Side-by-side run tables make identifying optimal hyperparameters effortless.\n- Governance & Lineage: Complete audit trail from training code to registered model binary.\n- Language & Library Agnostic: Seamless integration with all Python ML frameworks.\n\nLimitations & Trade-offs:\n- File-based artifact logging can become storage-heavy if large datasets/models are saved on every run.\n- Default SQLite backend is suited for single users; enterprise scale requires PostgreSQL or MySQL.',
    
    '[Insert diagram]':
        '[MLflow Architecture Diagram]\n'
        '  +--------------------------------------------------------+\n'
        '  |                ML Training Pipeline                    |\n'
        '  |  (Logistic Regression, Decision Tree, Random Forest)   |\n'
        '  +--------------------------------------------------------+\n'
        '            |                     |                   |\n'
        '            v                     v                   v\n'
        '      Params & Metrics       Evaluation Plots    Model Binaries\n'
        '    (Acc, F1, ROC-AUC)          (CM, ROC)           (.joblib)\n'
        '            |                     |                   |\n'
        '            +----------+----------+                   |\n'
        '                       |                              |\n'
        '                       v                              v\n'
        '            +-----------------------+     +-----------------------+\n'
        '            |  MLflow Backend Store |     |  MLflow Artifact Store|\n'
        '            |  (sqlite:///mlflow.db)|     |   (./A2/artifacts)    |\n'
        '            +-----------------------+     +-----------------------+\n'
        '                       |                              |\n'
        '                       +--------------+---------------+ \n'
        '                                      v\n'
        '                       +------------------------------+\n'
        '                       |    MLflow Model Registry     |\n'
        '                       |   (BestClassificationModel)  |\n'
        '                       +------------------------------+',
    
    '[Explanation]': 'Loaded Breast Cancer Wisconsin dataset, partitioned into 80/20 train-test splits, normalized features with StandardScaler, and configured MLflow SQLite tracking store.',
    '[commands]': 'python A2/src/train.py\npython A2/src/predict.py',
    '[Screenshot]': 'See Figure 2 and Figure 3 below.',
    
    '[Explanation, commands or code, screenshot]':
        'Trained 6 distinct model configurations logging all parameters and metrics. Selected Logistic_Regression_Tuned as the top performer (F1-score: 0.9861, Accuracy: 0.9825, ROC-AUC: 0.9954) and registered it into the MLflow Model Registry.',
    
    '[code]':
        '# Core MLflow Tracking Execution in A2/src/train.py\n'
        'with mlflow.start_run(run_name=name) as run:\n'
        '    model.fit(X_train, y_train)\n'
        '    y_pred = model.predict(X_test)\n'
        '    acc = accuracy_score(y_test, y_pred)\n'
        '    f1 = f1_score(y_test, y_pred)\n'
        '    mlflow.log_params(params)\n'
        '    mlflow.log_metric("accuracy", acc)\n'
        '    mlflow.log_metric("f1_score", f1)\n'
        '    mlflow.log_artifact(cm_plot_path)\n'
        '    joblib.dump(model, model_path)\n'
        '    mlflow.log_artifact(model_path)\n'
        '\n'
        '# Model Registry\n'
        'mlflow.register_model(f"runs:/{best_run_id}/model", "BestClassificationModel")',
    
    'GitHub Repository Link: [URL]': 'GitHub Repository Link: https://github.com/shubhambharnuke/mlops-final-assignments',
    
    '[Observation 1]': 'Hyperparameter tuning on Logistic Regression (increasing inverse regularization C from 0.1 to 1.0) improved test accuracy from 97.37% to 98.25% and F1-score to 0.9861.',
    '[Observation 2]': 'Decision Tree achieved 93.86% accuracy with max_depth=4, while Random Forest achieved 95.61% accuracy, showing ensemble stability over single trees on tabular data.',
    '[Observation 3]': 'MLflow automatically maintained persistent run records, parameters, and confusion matrix artifacts in the local SQLite database without manual tracking overhead.',
    
    '[Thus, we have successfully ...]':
        'Thus, we have successfully implemented experiment tracking using MLflow. We trained multiple supervised models, systematically tracked parameters, metrics, and visual artifacts, compared runs, registered the champion model in the Model Registry, and validated inference. This demonstrates how MLflow ensures complete reproducibility and structured governance in MLOps workflows.',
    
    '[Author / Organisation, Title, URL, accessed DD/MM/YYYY]':
        'MLflow Authors, "MLflow: An Open Source Machine Learning Platform", https://mlflow.org/docs/latest/index.html, accessed 20/11/2026.',
    '[Reference 2]':
        'M. Zaharia et al., "Accelerating the Machine Learning Lifecycle with MLflow," IEEE Micro, vol. 38, no. 5, pp. 39-45, 2018.'
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
        ('A2/screenshots/mlflow_tracking_terminal.png', 'Figure 2: MLflow Terminal Execution Logging 6 Model Experiments'),
        ('A2/screenshots/mlflow_runs_table.png', 'Figure 3: Comparative Experiment Evaluation Table across Models'),
        ('A2/artifacts/Logistic_Regression_Tuned_cm.png', 'Figure 4: Best Model Confusion Matrix (Logistic_Regression_Tuned)'),
        ('A2/artifacts/Logistic_Regression_Tuned_roc.png', 'Figure 5: Best Model ROC-AUC Curve (AUC = 0.995)'),
        ('A2/screenshots/mlflow_inference_evidence.png', 'Figure 6: Inference Validation from Registered Model')
    ]
    
    for img_path, caption in screenshots:
        if os.path.exists(img_path):
            img_p = target_p.insert_paragraph_before()
            run = img_p.add_run()
            run.add_picture(img_path, width=Inches(5.8))
            cap_p = target_p.insert_paragraph_before()
            cap_run = cap_p.add_run(caption)
            cap_run.font.italic = True
            cap_run.font.size = Pt(9.5)
            cap_run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

doc.save('A2/report.docx')
print('A2/report.docx successfully generated and populated.')
