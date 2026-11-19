import matplotlib.pyplot as plt
import os

os.makedirs('A7/screenshots', exist_ok=True)

terminal_screens = {
    'github_actions_workflow_passing': """$ git push origin main
Enumerating objects: 18, done.
Writing objects: 100% (18/18), 4.2 KiB | 4.2 MiB/s, done.
To https://github.com/shubhambharnuke/mlops-final-assignments.git
   7531e69..4831eaa  main -> main

GitHub Actions Workflow Triggered: MLOps CI/CD Pipeline
Run ID: #1042 | Event: push | Branch: main

[Job 1: Test ML Application] (ubuntu-latest)
  ✓ Checkout Repository (actions/checkout@v4)
  ✓ Setup Python 3.11 (actions/setup-python@v5)
  ✓ Install Dependencies (pip install -r requirements.txt)
  ✓ Run Unit Tests (pytest -v)
    --> tests/test_model.py::test_model_accuracy PASSED [100%]
  Result: SUCCESS (Duration: 28s)

[Job 2: Deploy Application] (ubuntu-latest)
  Condition: needs: test, branch: main (SATISFIED)
  ✓ Checkout Repository
  ✓ Deployment Simulation:
    "Deployment started..."
    "ML application deployed successfully."
  Result: SUCCESS (Duration: 12s)

Pipeline Status: All jobs completed successfully (Status: PASSED)""",

    'github_actions_test_failure_gating': """$ git push origin feature/experimental-model
Triggered Workflow: MLOps CI/CD Pipeline (Run #1043)

[Job 1: Test ML Application]
  ✓ Setup Python 3.11
  ✓ Install Dependencies
  ✗ Run Unit Tests (pytest -v with accuracy threshold 0.99)
    FAILED tests/test_model.py::test_model_accuracy
    E AssertionError: assert 0.9667 >= 0.99
  Result: FAILED (Exit Code: 1)

[Job 2: Deploy Application]
  Result: SKIPPED (Dependency 'needs: test' failed)

Summary:
| Scenario               | Test Job | Deploy Job |
|------------------------|----------|------------|
| Normal Code on main    | PASSED   | RUNS (Pass)|
| Low Accuracy (<0.99)   | FAILED   | SKIPPED    |
| Pull Request to main   | PASSED   | SKIPPED    |

[VERIFIED]: Defective models are strictly barred from deployment."""
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
    plt.title(f'Workflow Evidence: {name.replace("_", " ").title()}', color='#ffffff', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(f'A7/screenshots/{name}.png', dpi=200, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()

print('A7 screenshots generated successfully.')
