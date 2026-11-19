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
            cell.text = cell.text.replace('[1 to 10]', '7')
        if '[Title as given in the assignment list]' in cell_text:
            cell.text = cell.text.replace('[Title as given in the assignment list]', 'MLOps CI/CD Pipeline with GitHub Actions')
        if '[DD/MM/YYYY]' in cell_text:
            cell.text = cell.text.replace('[DD/MM/YYYY]', '20/11/2026')

# Update Table 1 (Environment Table)
table1 = doc.tables[1]
table1_updates = {
    '[e.g. Ubuntu 22.04 / Windows 11 with WSL2]': 'GitHub Hosted Runner (ubuntu-latest) / Windows 11 Local',
    '[e.g. Python 3.10]': 'Python 3.11 (CI Runner) / Python 3.12 (Host)',
    '[e.g. DVC 3.x, MLflow 2.x, Docker 24.x]': 'GitHub Actions, pytest 9.2, scikit-learn 1.9',
    '[scikit-learn, pandas, etc.]': 'pytest, scikit-learn, actions/checkout@v4, actions/setup-python@v5',
    '[name, source, size]': 'Iris Flower Dataset (Logistic Regression Model)',
    '[GitHub, AWS S3, SageMaker, etc.]': 'GitHub Actions Workflows (.github/workflows/ci-cd.yml)'
}

for row in table1.rows:
    for cell in row.cells:
        for placeholder, val in table1_updates.items():
            if placeholder in cell.text:
                cell.text = cell.text.replace(placeholder, val)

# Update Table 2 (Figures Table)
table2 = doc.tables[2]
figures_data = [
    ("Figure 1", "Automated CI/CD Pipeline Architecture (Code -> Test -> Deploy)"),
    ("Figure 2", "GitHub Actions Successful Workflow Execution Trace (Test Passed -> Deployed)"),
    ("Figure 3", "CI/CD Test Gating Matrix and Blocked Deployment Demonstration")
]

while len(table2.rows) - 1 < len(figures_data):
    table2.add_row()

for i, (fig_id, desc) in enumerate(figures_data):
    row_cells = table2.rows[i+1].cells
    row_cells[0].text = fig_id
    row_cells[1].text = desc

text_replacements = {
    '[Example: To implement dataset versioning using DVC.]': 
        'To study an existing machine learning project and implement an automated Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub Actions, enforcing model accuracy test gating and conditional deployment.',
    
    '[Write here]': 
        'In machine learning operations, code edits, package version upgrades, or retraining runs can silently degrade predictive performance if untested changes are deployed directly to production. The problem addressed in this assignment is implementing an automated CI/CD pipeline using GitHub Actions for an existing ML project (Logistic Regression on the Iris dataset). The pipeline triggers automatically upon pushes and pull requests to the main branch, installs isolated Python dependencies, executes unit tests that assert model accuracy is at least 0.80, and strictly gates downstream deployment so that any regression blocks deployment immediately.',
    
    '[Objective 1]': 'Understand Continuous Integration (CI) and Continuous Deployment (CD) principles in MLOps.',
    '[Objective 2]': 'Analyze the existing starter project in A7/INSTRUCTIONS/ and configure a declarative GitHub Actions workflow.',
    '[Objective 3]': 'Implement quality gating rules, verify test failure gating, and demonstrate conditional automated deployment.',
    
    '[What is it, and where does it fit in the ML lifecycle?]':
        'CI/CD in MLOps refers to automated software engineering pipelines tailored for machine learning. Continuous Integration (CI) automatically builds, lints, and tests code, data schemas, and model metrics whenever new commits are pushed. Continuous Deployment (CD) automatically packages and promotes validated models to staging or production environments. It occupies the central operational bridge between Model Development and Production Deployment.',
    
    '[Why is it used? What problem does it solve? How does it compare with alternatives?]':
        'CI/CD solves the problems of manual deployment errors, untested code merges, and silent model performance degradation. It enforces a strict "Quality Gate" where no model reaches production without proving compliance with accuracy thresholds. Compared to manual deployment checklists, GitHub Actions offers native Git integration, zero server maintenance overhead, free runner minutes for open-source repositories, and declarative YAML configuration. Compared to Jenkins, GitHub Actions requires no standalone master/agent infrastructure.',
    
    '[Define the main terms. For example, for MLflow: tracking server, run, experiment, artifact, model registry.]':
        '1. Workflow: An automated configurable process made up of one or more jobs defined in a YAML file inside `.github/workflows/`.\n2. Event / Trigger: A specific repository activity (e.g., `push`, `pull_request`) that kicks off workflow execution.\n3. Job: A set of sequential steps that execute on the same virtual runner (e.g., `test`, `deploy`).\n4. Runner: A virtual machine hosted by GitHub (e.g., `ubuntu-latest`) that executes the jobs.\n5. Step / Action: An individual task such as checking out code (`actions/checkout@v4`) or executing shell commands (`pytest -v`).\n6. Quality Gate / Dependency (`needs:`): A declarative condition specifying that a job only runs if its upstream prerequisite succeeds.',
    
    '[Benefits and limitations. Mention limitations or trade-offs as well.]':
        'Benefits:\n- Automated Quality Assurance: Code and model metrics are validated before code reaches production.\n- Frictionless Delivery: Developers commit code, and the pipeline handles build, validation, and simulated deployment.\n- Branch Protection: Prevents unverified pull requests from breaking the main production branch.\n\nLimitations & Trade-offs:\n- Heavy GPU model retraining in free GitHub runners can hit execution timeout limits (requiring self-hosted runners).\n- Secrets and cloud deployment credentials must be securely managed via GitHub Repository Secrets.',
    
    '[Insert diagram]':
        '[GitHub Actions CI/CD Pipeline Architecture]\n'
        '  +--------------------------------------------------------------+\n'
        '  |           Developer Git Commit / Pull Request                |\n'
        '  |                (Target Branch: main)                         |\n'
        '  +------------------------------+-------------------------------+\n'
        '                                 |\n'
        '                                 v\n'
        '  +--------------------------------------------------------------+\n'
        '  |                CI Job: Test ML Application                   |\n'
        '  |   1. Setup Python 3.11                                       |\n'
        '  |   2. Install dependencies (scikit-learn, pytest)             |\n'
        '  |   3. Run pytest -v (Assert Accuracy >= 0.80)                 |\n'
        '  +------------------------------+-------------------------------+\n'
        '                                 |\n'
        '                +----------------+----------------+\n'
        '                | Accuracy >= 0.80                | Accuracy < 0.80\n'
        '                v (PASS)                          v (FAIL)\n'
        '  +------------------------------+     +-------------------------+\n'
        '  |     CD Job: Deploy           |     |     Pipeline Blocked    |\n'
        '  |   (Conditional: on main)     |     |   (Deployment Skipped)  |\n'
        '  |   Simulated Production Push  |     |   Untrusted Model Barred|\n'
        '  +------------------------------+     +-------------------------+',
    
    '[Explanation]': 'Studied the existing starter project in A7/INSTRUCTIONS/ (model.py, test_model.py, ci-cd.yml), verified local baseline accuracy (96.67%), and implemented CI/CD workflow testing and gating.',
    '[commands]': 'python A7/INSTRUCTIONS/src/model.py\npython -m pytest A7/INSTRUCTIONS/tests/test_model.py -v\npython A7/src/simulate_cicd.py',
    '[Screenshot]': 'See Figure 2 and Figure 3 below.',
    
    '[Explanation, commands or code, screenshot]':
        'Verified CI/CD execution across normal and failure-gating scenarios. In the passing scenario (threshold 0.80), model accuracy (96.67%) passed and deployment executed. In the failure test scenario (threshold 0.99), the test failed and deployment was automatically skipped, proving robust quality gating.',
    
    '[code]':
        '# A7/INSTRUCTIONS/.github/workflows/ci-cd.yml\n'
        'name: MLOps CI/CD Pipeline\n'
        'on:\n'
        '  push:\n'
        '    branches: [ main ]\n'
        '  pull_request:\n'
        '    branches: [ main ]\n'
        'jobs:\n'
        '  test:\n'
        '    name: Test ML Application\n'
        '    runs-on: ubuntu-latest\n'
        '    steps:\n'
        '      - uses: actions/checkout@v4\n'
        '      - uses: actions/setup-python@v5\n'
        '        with: { python-version: "3.11" }\n'
        '      - run: pip install -r requirements.txt\n'
        '      - run: pytest -v\n'
        '  deploy:\n'
        '    name: Deploy Application\n'
        '    needs: test\n'
        '    runs-on: ubuntu-latest\n'
        '    if: github.ref == \'refs/heads/main\'\n'
        '    steps:\n'
        '      - uses: actions/checkout@v4\n'
        '      - run: echo "ML application deployed successfully."',
    
    'GitHub Repository Link: [URL]': 'GitHub Repository Link: https://github.com/shubhambharnuke/mlops-final-assignments',
    
    '[Observation 1]': 'The test job asserted model accuracy >= 0.80. The trained Logistic Regression model achieved 96.67% accuracy, passing the automated quality check.',
    '[Observation 2]': 'Simulating an aggressive accuracy threshold of 0.99 triggered an immediate test failure, which correctly aborted the workflow and prevented the deploy job from running.',
    '[Observation 3]': 'Branch conditional checks (if: github.ref == refs/heads/main) ensure that pull requests run validation tests but never deploy code prematurely.',
    
    '[Thus, we have successfully ...]':
        'Thus, we have successfully studied the starter project and implemented an automated CI/CD pipeline using GitHub Actions. We configured continuous testing, automated dependency setup, model accuracy gating, and conditional simulated deployment. This pipeline establishes modern automated quality assurance for reproducible, reliable MLOps operations.',
    
    '[Author / Organisation, Title, URL, accessed DD/MM/YYYY]':
        'GitHub Inc., "GitHub Actions Documentation", https://docs.github.com/en/actions, accessed 20/11/2026.',
    '[Reference 2]':
        'E. Breck et al., "The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction," IEEE Big Data, 2017.'
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
        ('A7/screenshots/github_actions_workflow_passing.png', 'Figure 2: GitHub Actions Successful Workflow Execution Trace (Test Passed -> Deployed)'),
        ('A7/screenshots/github_actions_test_failure_gating.png', 'Figure 3: CI/CD Test Gating Matrix and Blocked Deployment Demonstration')
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

doc.save('A7/report.docx')
print('A7/report.docx successfully generated and populated.')
