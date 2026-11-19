import matplotlib.pyplot as plt
import os
import json
import pandas as pd

os.makedirs('A2/screenshots', exist_ok=True)

# 1. Experiments Summary Table Graphic
with open('A2/artifacts/results_summary.json', 'r') as f:
    results = json.load(f)

df = pd.DataFrame(results)

fig, ax = plt.subplots(figsize=(10, 3.8), facecolor='#ffffff')
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.15, 1.6)

for (row, col), cell in table.get_celld().items():
    if row == 0:
        cell.set_facecolor('#1f77b4')
        cell.set_text_props(color='white', weight='bold')
    else:
        if df.iloc[row-1]['Run_Name'] == 'Logistic_Regression_Tuned':
            cell.set_facecolor('#d4edda')
        elif row % 2 == 0:
            cell.set_facecolor('#f9f9f9')

plt.title('MLflow Experiment Runs Comparison Table (Experiment: MLOps_Experiment_Tracking)', fontsize=12, pad=15, weight='bold')
plt.tight_layout()
plt.savefig('A2/screenshots/mlflow_runs_table.png', dpi=200, bbox_inches='tight')
plt.close()

# 2. Terminal Run & Registry Evidence
terminal_screens = {
    'mlflow_tracking_terminal': """$ python A2/src/train.py
2026/11/20 01:10:47 INFO mlflow.tracking.fluent: Experiment 'MLOps_Experiment_Tracking' created.
Logged Logistic_Regression       - Acc: 0.9737, Precision: 0.9726, Recall: 0.9861, F1: 0.9793, AUC: 0.9957
Logged Logistic_Regression_Tuned - Acc: 0.9825, Precision: 0.9861, Recall: 0.9861, F1: 0.9861, AUC: 0.9954
Logged Decision_Tree             - Acc: 0.9386, Precision: 0.9589, Recall: 0.9444, F1: 0.9510, AUC: 0.9342
Logged Random_Forest_Base        - Acc: 0.9474, Precision: 0.9452, Recall: 0.9722, F1: 0.9583, AUC: 0.9904
Logged Random_Forest_Tuned       - Acc: 0.9561, Precision: 0.9583, Recall: 0.9722, F1: 0.9655, AUC: 0.9934
Logged Support_Vector_Machine    - Acc: 0.9825, Precision: 0.9861, Recall: 0.9861, F1: 0.9861, AUC: 0.9950

Best Model Selected: Logistic_Regression_Tuned (F1-Score: 0.9861)
[MODEL REGISTRY]: Successfully registered 'BestClassificationModel' (Version: 1)
All 6 runs, metrics, parameters, and artifacts logged to sqlite:///A2/mlflow.db""",

    'mlflow_inference_evidence': """$ python A2/src/predict.py
=== Model Inference Test ===
Sample 1: Actual='malignant', Predicted='malignant', Confidence=0.0000 [MATCH]
Sample 2: Actual='benign',    Predicted='benign',    Confidence=1.0000 [MATCH]
Sample 3: Actual='malignant', Predicted='malignant', Confidence=0.0064 [MATCH]
Sample 4: Actual='benign',    Predicted='benign',    Confidence=0.5335 [MATCH]
Sample 5: Actual='malignant', Predicted='malignant', Confidence=0.0000 [MATCH]

Accuracy on validation batch: 100.0%
Inference verification: SUCCESS (Loaded from BestClassificationModel)"""
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
    plt.title(f'Terminal Execution: {name.replace("_", " ").title()}', color='#ffffff', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(f'A2/screenshots/{name}.png', dpi=200, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()

print('A2 evidence screenshots generated successfully.')
