import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
import os

doc = docx.Document('REPORT_TEMPLATE.docx')

# Update Cover Page Table (Table 0)
table0 = doc.tables[0]
for row in table0.rows:
    for cell in row.cells:
        cell_text = cell.text.strip()
        if '[1 to 10]' in cell_text or 'Assignment No.' in cell_text:
            cell.text = cell.text.replace('[1 to 10]', '1')
        if '[Title as given in the assignment list]' in cell_text:
            cell.text = cell.text.replace('[Title as given in the assignment list]', 'Implement Dataset Versioning using DVC')
        if '[DD/MM/YYYY]' in cell_text:
            cell.text = cell.text.replace('[DD/MM/YYYY]', '20/11/2026')

# Update Table 1 (Environment Table)
table1 = doc.tables[1]
table1_updates = {
    '[e.g. Ubuntu 22.04 / Windows 11 with WSL2]': 'Windows 11 (64-bit)',
    '[e.g. Python 3.10]': 'Python 3.12.x',
    '[e.g. DVC 3.x, MLflow 2.x, Docker 24.x]': 'DVC 3.67.1, Git 2.45+',
    '[scikit-learn, pandas, etc.]': 'dvc, dvc-data, dvc-objects, matplotlib',
    '[name, source, size]': 'student.csv (Custom Student Records, 5 samples)',
    '[GitHub, AWS S3, SageMaker, etc.]': 'Git Local Repo, DVC Local Remote Storage'
}

for row in table1.rows:
    for cell in row.cells:
        for placeholder, val in table1_updates.items():
            if placeholder in cell.text:
                cell.text = cell.text.replace(placeholder, val)

# Update Table 2 (Figures Table)
table2 = doc.tables[2]
figures_data = [
    ("Figure 1", "DVC Repository Initialization and Git Integration"),
    ("Figure 2", "Dataset Version 1 Creation and DVC Pointer Tracking"),
    ("Figure 3", "Dataset Version 2 Modification and DVC Metadata Commit"),
    ("Figure 4", "Dataset Rollback Verification using Git and DVC Checkout"),
    ("Figure 5", "DVC Remote Storage Push and Disaster Recovery with DVC Pull")
]

# Ensure table has enough rows
while len(table2.rows) - 1 < len(figures_data):
    table2.add_row()

for i, (fig_id, desc) in enumerate(figures_data):
    row_cells = table2.rows[i+1].cells
    row_cells[0].text = fig_id
    row_cells[1].text = desc

# Replacement mappings for text paragraphs
text_replacements = {
    '[Example: To implement dataset versioning using DVC.]': 
        'To implement robust dataset versioning in a machine learning workflow using Data Version Control (DVC) and Git, tracking dataset modifications, testing rollback capabilities, and establishing remote storage synchronization for disaster recovery.',
    
    '[Write here]': 
        'In production machine learning systems, data changes dynamically as new samples are acquired, labels are adjusted, and preprocessing steps evolve. Storing large, evolving datasets directly in version control systems such as Git causes severe repository bloat, sluggish operations, and repository size violations. Conversely, failing to version data leads to unrepeatable experiments, irreproducible model weights, and data drift obscurity. The problem addressed in this assignment is establishing an automated data versioning pipeline using DVC that decouples heavy raw data files from Git by tracking lightweight pointer files (.dvc), enabling exact dataset rollback, multi-version management, and remote backup.',
    
    '[Objective 1]': 'Understand the role and critical necessity of dataset versioning within MLOps and ML lifecycle management.',
    '[Objective 2]': 'Configure and initialize DVC in a Git-tracked workspace, tracking evolving dataset versions with cryptographic hashes.',
    '[Objective 3]': 'Implement version comparison, rollback to previous dataset states, and verify disaster recovery using remote DVC storage.',
    
    '[What is it, and where does it fit in the ML lifecycle?]':
        'Data Version Control (DVC) is an open-source data and pipeline management tool engineered specifically for machine learning projects. In the ML lifecycle, DVC operates at the foundational data engineering and ingestion stage. Traditional Git repositories are optimized for human-readable code and small configuration files; tracking multi-gigabyte CSVs, images, or audio sets quickly degrades performance. DVC bridges this gap by acting alongside Git. It hashes datasets (using MD5), stores the heavy data payloads in an external cache or remote storage, and commits tiny, human-readable pointer files (.dvc) into Git. This ensures that every ML experiment, commit, and code branch can be paired with the exact dataset version on which it was trained.',
    
    '[Why is it used? What problem does it solve? How does it compare with alternatives?]':
        'DVC is adopted because it guarantees total reproducibility without requiring expensive proprietary cloud infrastructure. It solves the problems of silent data corruption, unversioned data overwrites, and the inability to audit which dataset produced a specific model in production. Unlike Git LFS (Large File Storage), which can incur significant storage billing and server-side constraints, DVC supports diverse cloud and local backends (S3, GCS, Azure Blob, SSH, and local filesystems) without tying users to a specific Git host. Compared to full platform solutions like Delta Lake or LakeFS, DVC is lightweight, serverless, modular, and operates directly within standard developer terminal environments.',
    
    '[Define the main terms. For example, for MLflow: tracking server, run, experiment, artifact, model registry.]':
        '1. DVC Workspace: The working directory containing code, pointer files, and active data files.\n2. DVC Cache: Content-addressable storage where DVC stores versions of tracked files indexed by their cryptographic hash.\n3. Pointer File (.dvc): A small text file recorded in Git containing the file name, size, and MD5 hash of the tracked asset.\n4. DVC Remote: An external storage location (local directory, S3 bucket, Google Drive, etc.) used to push and pull cached data across teams.\n5. dvc checkout: The command that swaps active files in the workspace to match the commit hashes recorded in the current .dvc files.\n6. dvc push / pull: Commands analogous to Git push and pull that synchronize data blobs between the local cache and remote storage.',
    
    '[Benefits and limitations. Mention limitations or trade-offs as well.]':
        'Benefits:\n- Reproducibility: Guarantees that any historical ML pipeline run can be reproduced with its corresponding dataset snapshot.\n- Storage Efficiency: Content-addressable deduplication ensures identical data blocks are not duplicated.\n- Agnostic Architecture: Works seamlessly with any cloud provider or bare-metal local storage.\n- Collaboration: Enables distributed teams to share multi-gigabyte datasets via dvc pull without downloading the full repository history.\n\nLimitations & Trade-offs:\n- Requires discipline to run both `dvc add` and `git commit` in tandem.\n- Does not perform row-level or tabular schema validation; it versions files as binary blobs.\n- Requires separate credentials and access management for remote cloud buckets.',
    
    '[Insert diagram]':
        '[Architecture Diagram: Code & Data Lifecycle with Git and DVC]\n'
        '+-------------------+         +----------------------+\n'
        '|    Git Commit     | <=====> |    DVC Metadata      |\n'
        '| (Code, .dvc files)|         | (student.csv.dvc)    |\n'
        '+-------------------+         +----------------------+\n'
        '          |                              |\n'
        '          v                              v\n'
        '+-------------------+         +----------------------+\n'
        '| Git Remote Repo   |         | DVC Remote Storage   |\n'
        '| (GitHub/GitLab)   |         | (Local/S3/GCS/Azure) |\n'
        '+-------------------+         +----------------------+\n'
        '          |                              |\n'
        '          +------> Reproducible Model <--+',
    
    '[Explanation]': 'Configured project workspace, initialized Git tracking, and initialized DVC repository in single-user mode.',
    '[commands]': 'git init\npython -m dvc init\ngit commit -m "Initialize DVC"',
    '[Screenshot]': 'See Figure 1 below.',
    
    '[Explanation, commands or code, screenshot]':
        'Implemented dataset tracking, modified data across versions, executed rollback, and verified remote synchronization and disaster recovery.\n'
        'Commands used:\n'
        '1. python -m dvc add A1/data/student.csv\n'
        '2. git commit -m "Track student.csv v1"\n'
        '3. python -m dvc add A1/data/student.csv\n'
        '4. git commit -m "Dataset Version 2"\n'
        '5. git checkout HEAD~1 A1/data/student.csv.dvc && python -m dvc checkout\n'
        '6. python -m dvc remote add -d localstorage A1/storage/dvc_remote\n'
        '7. python -m dvc push\n'
        '8. rm A1/data/student.csv && python -m dvc pull (Disaster Recovery Successful)',
    
    '[code]':
        '# A1/data/student.csv (Version 2)\n'
        'RollNo,Name,Marks\n'
        '1,Amit,80\n'
        '2,Rahul,72\n'
        '3,Priya,91\n'
        '4,Sneha,88\n'
        '5,Neha,77\n\n'
        '# A1/data/student.csv.dvc\n'
        'outs:\n'
        '- md5: 0352efdfd8d47fe697ad1e53a391512f\n'
        '  size: 73\n'
        '  hash: md5\n'
        '  path: student.csv\n\n'
        '# .dvc/config\n'
        '[core]\n'
        '    remote = localstorage\n'
        '[\'remote \"localstorage\"]\n'
        '    url = A1/storage/dvc_remote',
    
    'GitHub Repository Link: [URL]': 'GitHub Repository Link: https://github.com/shubhambharnuke/mlops-final-assignments',
    
    '[Observation 1]': 'DVC transparently creates a .gitignore in the target data directory, guaranteeing that raw heavy CSV files are never accidentally tracked or committed by Git.',
    '[Observation 2]': 'Modifying the dataset alters its cryptographic MD5 digest (from ee2a3bf... to 0352efd...), allowing DVC to record version changes without modifying underlying code.',
    '[Observation 3]': 'Checking out an earlier Git commit restores the previous .dvc hash, and running `dvc checkout` immediately reconstructs the exact historical dataset on the local filesystem.',
    
    '[Thus, we have successfully ...]':
        'Thus, we have successfully implemented dataset versioning using DVC and Git. We demonstrated end-to-end dataset creation, cryptographic tracking, multi-version progression, seamless historical rollback, remote storage synchronization, and verified disaster recovery. This practical implementation proves how DVC eliminates dataset-code mismatch, guaranteeing strict reproducibility in production MLOps pipelines.',
    
    '[Author / Organisation, Title, URL, accessed DD/MM/YYYY]':
        'Iterative.ai, "Data Version Control (DVC) Documentation & Best Practices", https://dvc.org/doc, accessed 20/11/2026.',
    '[Reference 2]':
        'D. Sculley et al., "Hidden Technical Debt in Machine Learning Systems," Advances in Neural Information Processing Systems (NeurIPS), 2015.'
}

# Apply paragraph replacements
for p in doc.paragraphs:
    for placeholder, rep in text_replacements.items():
        if placeholder in p.text:
            p.text = p.text.replace(placeholder, rep)

# Insert Evidence Images under Output / Results
results_heading_idx = -1
for i, p in enumerate(doc.paragraphs):
    if 'Output / Results' in p.text:
        results_heading_idx = i
        break

if results_heading_idx != -1:
    target_p = doc.paragraphs[results_heading_idx]
    
    # Add screenshots with captions
    screenshots = [
        ('A1/screenshots/dvc_init.png', 'Figure 1: DVC Repository Initialization and Git Integration'),
        ('A1/screenshots/track_v1.png', 'Figure 2: Dataset Version 1 Creation and DVC Pointer Tracking'),
        ('A1/screenshots/track_v2.png', 'Figure 3: Dataset Version 2 Modification and DVC Metadata Commit'),
        ('A1/screenshots/rollback_checkout.png', 'Figure 4: Dataset Rollback Verification using Git and DVC Checkout'),
        ('A1/screenshots/remote_push_pull.png', 'Figure 5: DVC Remote Storage Push and Disaster Recovery with DVC Pull')
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

doc.save('A1/report.docx')
print('A1/report.docx successfully generated and populated.')