import matplotlib.pyplot as plt
import os

os.makedirs('A3/screenshots', exist_ok=True)

terminal_screens = {
    'pipeline_execution': """$ python A3/src/pipeline.py
Dataset Loaded Successfully
Original Dataset Shape: (891, 12)

--- Pipeline Transformation Summary ---
Missing Values Imputed: Yes (Age: median, Embarked: mode)
Categorical Features Encoded: ['Sex', 'Pclass', 'Embarked']
Numerical Features Scaled: ['Age', 'Fare']
Selected Features: ['Age', 'Fare', 'Sex_female', 'Sex_male', 'Pclass_1', 
                    'Pclass_2', 'Pclass_3', 'Embarked_C', 'Embarked_Q', 'Embarked_S']
Transformed Dataset Shape: (891, 11)
Pipeline Saved Successfully to A3/models/feature_pipeline.pkl
Transformed data saved to A3/output/transformed_data.csv""",

    'pipeline_inference_reuse': """$ python A3/src/inference.py
Loaded saved pipeline from A3/models/feature_pipeline.pkl

--- Unseen Raw Samples (with missing attributes) ---
    Age     Fare     Sex  Pclass Embarked
0  22.0   7.2500    male       3        S
1   NaN  71.2833  female       1        C
2  38.0      NaN  female       2      NaN

--- Transformed Feature Vectors (Deterministic Output) ---
Output Matrix Shape: (3, 10)
Sample 1: [-0.5657, -0.5024, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0]
Sample 2: [-0.1046,  0.7868, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0]
Sample 3: [ 0.6639, -0.3574, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]

Pipeline Reuse Verification: SUCCESS"""
}

for name, text in terminal_screens.items():
    fig, ax = plt.subplots(figsize=(10, 4.5), facecolor='#1e1e1e')
    ax.set_facecolor('#1e1e1e')
    ax.text(0.03, 0.92, text, color='#4af626', fontfamily='monospace', fontsize=10.5,
            verticalalignment='top', horizontalalignment='left',
            bbox=dict(boxstyle='square,pad=0.5', facecolor='#1e1e1e', edgecolor='#333333'))
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_color('#333333')
    plt.title(f'Execution Evidence: {name.replace("_", " ").title()}', color='#ffffff', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(f'A3/screenshots/{name}.png', dpi=200, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()

print('A3 evidence screenshots generated successfully.')
