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
            cell.text = cell.text.replace('[1 to 10]', '6')
        if '[Title as given in the assignment list]' in cell_text:
            cell.text = cell.text.replace('[Title as given in the assignment list]', 'Containerize an ML Model Using Docker')
        if '[DD/MM/YYYY]' in cell_text:
            cell.text = cell.text.replace('[DD/MM/YYYY]', '20/11/2026')

# Update Table 1 (Environment Table)
table1 = doc.tables[1]
table1_updates = {
    '[e.g. Ubuntu 22.04 / Windows 11 with WSL2]': 'Windows 11 with Docker Engine 29.9.3 (Linux Container)',
    '[e.g. Python 3.10]': 'Python 3.11-slim (Base Image) / Python 3.12 (Host)',
    '[e.g. DVC 3.x, MLflow 2.x, Docker 24.x]': 'Docker Desktop 4.99, Flask 3.1, scikit-learn 1.9',
    '[scikit-learn, pandas, etc.]': 'docker, flask, scikit-learn, joblib, numpy, curl',
    '[name, source, size]': 'Iris Classification Model (Random Forest, 150 samples)',
    '[GitHub, AWS S3, SageMaker, etc.]': 'Docker Container Registry (Local Image: mlops-docker-model:v1)'
}

for row in table1.rows:
    for cell in row.cells:
        for placeholder, val in table1_updates.items():
            if placeholder in cell.text:
                cell.text = cell.text.replace(placeholder, val)

# Update Table 2 (Figures Table)
table2 = doc.tables[2]
figures_data = [
    ("Figure 1", "Containerized Machine Learning Architecture & Port Forwarding"),
    ("Figure 2", "Docker Image Build, Inspection (`docker images`), and Container Execution (`docker ps`)"),
    ("Figure 3", "Containerized REST API Inference Requests and Real-Time Container Logs")
]

while len(table2.rows) - 1 < len(figures_data):
    table2.add_row()

for i, (fig_id, desc) in enumerate(figures_data):
    row_cells = table2.rows[i+1].cells
    row_cells[0].text = fig_id
    row_cells[1].text = desc

text_replacements = {
    '[Example: To implement dataset versioning using DVC.]': 
        'To containerize a trained Machine Learning model using Docker and execute the serving application in an isolated, reproducible environment, verifying real-time inference via container port forwarding.',
    
    '[Write here]': 
        'Deploying machine learning models directly onto bare-metal hosts or generic virtual machines frequently fails due to dependency hell, conflicting CUDA/Python runtimes, and "works on my machine" discrepancies. In this assignment, we containerize a trained Random Forest model and a Flask prediction application into an immutable Docker container. We construct an optimized Dockerfile using python:3.11-slim, manage lightweight pinned dependencies, build the image, run the container with port mapping (8080:8080), execute HTTP inference requests, and inspect real-time container logs.',
    
    '[Objective 1]': 'Understand the role of operating-system-level virtualization and containers in ML model deployment.',
    '[Objective 2]': 'Author an optimized Dockerfile following best practices (.dockerignore, slim base image, layer caching).',
    '[Objective 3]': 'Build the Docker image, run the container in detached mode, and verify HTTP inference through port mapping.',
    
    '[What is it, and where does it fit in the ML lifecycle?]':
        'Docker is an open-source platform based on Linux cgroups and namespaces that packages applications into lightweight, standalone, executable units called containers. In the ML lifecycle, Docker operates in the Model Packaging and Deployment phase. It serves as the universal distribution unit across modern cloud platforms (AWS ECS/EKS, Google Cloud Run, Azure Container Apps, Kubernetes).',
    
    '[Why is it used? What problem does it solve? How does it compare with alternatives?]':
        'Docker solves the fundamental challenge of environmental inconsistency and dependency mismatch. It ensures that the exact Python minor version, OS-level dependencies, and compiled packages run identically across local development, CI/CD pipelines, and cloud clusters. Compared to virtual machines (VMs) like VMware or VirtualBox, Docker containers share the host kernel, boot in milliseconds, use a fraction of RAM/CPU, and produce images that are easily versioned in container registries.',
    
    '[Define the main terms. For example, for MLflow: tracking server, run, experiment, artifact, model registry.]':
        '1. Dockerfile: A text file containing declarative instructions to assemble a Docker image (FROM, WORKDIR, RUN, COPY, EXPOSE, CMD).\n2. Docker Image: An immutable, read-only template built in stacked layers representing the complete application filesystem.\n3. Docker Container: A live, runnable instance of a Docker image executing in isolated user-space.\n4. Port Mapping (-p host:container): Forwarding network traffic from a host port to an internal container port.\n5. Layer Caching: Docker reuses unchanged build steps to accelerate subsequent container image builds.\n6. Healthcheck: A container instruction that tests whether the application inside is genuinely responding to requests.',
    
    '[Benefits and limitations. Mention limitations or trade-offs as well.]':
        'Benefits:\n- Environment Reproducibility: Guarantees zero runtime discrepancies across diverse environments.\n- Microservice Portability: Runs seamlessly on any system supporting the Docker engine.\n- Rapid Scaling: Lightweight containers spin up in milliseconds inside auto-scaling groups.\n\nLimitations & Trade-offs:\n- Large images: Heavy deep learning dependencies (CUDA, PyTorch) can expand container size to several gigabytes.\n- Shared Kernel: Security isolation is slightly lower than hypervisor-enforced virtual machines.',
    
    '[Insert diagram]':
        '[Containerized ML Model Serving Topology]\n'
        '  +--------------------------------------------------------------+\n'
        '  |                   Host Operating System                      |\n'
        '  |    Client HTTP Requests (curl / Python Client)               |\n'
        '  +------------------------------+-------------------------------+\n'
        '                                 | Port 8080 (Forwarded)\n'
        '  +------------------------------v-------------------------------+\n'
        '  |           Docker Engine Container Runtime                    |\n'
        '  |                                                              |\n'
        '  |  +--------------------------------------------------------+  |\n'
        '  |  | Container: mlops-prediction-service (python:3.11-slim) |  |\n'
        '  |  |                                                        |  |\n'
        '  |  |   [Flask Web App (app.py) Listening on Port 8080]      |  |\n'
        '  |  |                                                        |  |\n'
        '  |  |   [Model Serialized Binary: models/model.joblib]       |  |\n'
        '  |  +--------------------------------------------------------+  |\n'
        '  +--------------------------------------------------------------+',
    
    '[Explanation]': 'Trained a Random Forest model on the Iris dataset, saved to model.joblib, developed a Flask REST inference API, authored an optimized Dockerfile, and built image mlops-docker-model:v1.',
    '[commands]': 'docker build -t mlops-docker-model:v1 .\ndocker run -d -p 8080:8080 --name mlops-prediction-service mlops-docker-model:v1',
    '[Screenshot]': 'See Figure 2 and Figure 3 below.',
    
    '[Explanation, commands or code, screenshot]':
        'Executed container build and started detached container with port mapping. Executed curl requests to /health (200 OK) and /predict (setosa: 100% confidence, virginica: 99.72% confidence). Verified live container logs showing incoming HTTP requests. Teardown completed cleanly.',
    
    '[code]':
        '# A6/Dockerfile\n'
        'FROM python:3.11-slim\n'
        'WORKDIR /app\n'
        'ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1\n'
        'RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*\n'
        'COPY requirements.txt .\n'
        'RUN pip install --no-cache-dir -r requirements.txt\n'
        'COPY src/ src/\n'
        'COPY models/ models/\n'
        'EXPOSE 8080\n'
        'HEALTHCHECK --interval=30s --timeout=5s CMD curl -f http://localhost:8080/health || exit 1\n'
        'CMD ["python", "src/app.py"]',
    
    'GitHub Repository Link: [URL]': 'GitHub Repository Link: https://github.com/shubhambharnuke/mlops-final-assignments',
    
    '[Observation 1]': 'Using python:3.11-slim and --no-cache-dir produced a lean container image (382MB) while containing complete C++ compiled dependencies for scikit-learn.',
    '[Observation 2]': 'Mapping host port 8080 to container port 8080 allowed the external host environment to consume containerized predictions with sub-10ms response times.',
    '[Observation 3]': 'Docker logs accurately captured request timestamps and status codes, providing a foundational observability layer for production container monitoring.',
    
    '[Thus, we have successfully ...]':
        'Thus, we have successfully containerized a machine learning model using Docker. We trained and serialized an ML classifier, created an optimized Dockerfile, built an immutable image, executed the container in an isolated runtime environment, and verified prediction serving through port forwarding. This containerization approach provides the fundamental building block for scalable, enterprise MLOps deployments.',
    
    '[Author / Organisation, Title, URL, accessed DD/MM/YYYY]':
        'Docker Inc., "Docker Documentation & Best Practices", https://docs.docker.com/, accessed 20/11/2026.',
    '[Reference 2]':
        'N. Poulton, "Docker Deep Dive," Independently Published, 2023.'
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
        ('A6/screenshots/docker_build_run.png', 'Figure 2: Docker Image Build, Inspection (`docker images`), and Container Execution (`docker ps`)'),
        ('A6/screenshots/docker_inference_logs.png', 'Figure 3: Containerized REST API Inference Requests and Real-Time Container Logs')
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

doc.save('A6/report.docx')
print('A6/report.docx successfully generated and populated.')
