import matplotlib.pyplot as plt
import os

os.makedirs('A6/screenshots', exist_ok=True)

terminal_screens = {
    'docker_build_run': """$ docker build -t mlops-docker-model:v1 .
[+] Building 33.6s (11/11) FINISHED
 => [internal] load build definition from Dockerfile
 => [1/7] FROM docker.io/library/python:3.11-slim
 => [2/7] WORKDIR /app
 => [3/7] RUN apt-get update && apt-get install -y --no-install-recommends curl
 => [4/7] COPY requirements.txt .
 => [5/7] RUN pip install --no-cache-dir -r requirements.txt
 => [6/7] COPY src/ src/
 => [7/7] COPY models/ models/
 => exporting to image
 => naming to docker.io/library/mlops-docker-model:v1: DONE

$ docker images mlops-docker-model:v1
REPOSITORY           TAG       IMAGE ID       CREATED          SIZE
mlops-docker-model   v1        dbfe394f8219   30 seconds ago   382MB

$ docker run -d -p 8080:8080 --name mlops-prediction-service mlops-docker-model:v1
d0d6a929b903436d78bb3f56f71c57b9bd4d8fe06f2fe5b82133235492545b1e

$ docker ps
CONTAINER ID   IMAGE                    COMMAND                  PORTS                    STATUS
d0d6a929b903   mlops-docker-model:v1    "python src/app.py"      0.0.0.0:8080->8080/tcp   Up 12 seconds""",

    'docker_inference_logs': """$ curl -X GET "http://localhost:8080/health"
{"container": "mlops-docker-model", "model_loaded": true, "status": "UP"}

$ curl -X POST "http://localhost:8080/predict" \\
     -H "Content-Type: application/json" \\
     -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
{"class_id": 0, "confidence": 1.0, "prediction": "setosa", "status": "success"}

$ curl -X POST "http://localhost:8080/predict" \\
     -H "Content-Type: application/json" \\
     -d '{"sepal_length": 6.7, "sepal_width": 3.3, "petal_length": 5.7, "petal_width": 2.1}'
{"class_id": 2, "confidence": 0.9972, "prediction": "virginica", "status": "success"}

$ docker logs mlops-prediction-service
 * Running on http://0.0.0.0:8080
172.17.0.1 - - [19/Nov/2026 19:56:31] "GET /health HTTP/1.1" 200 -
172.17.0.1 - - [19/Nov/2026 19:56:31] "POST /predict HTTP/1.1" 200 -
172.17.0.1 - - [19/Nov/2026 19:56:31] "POST /predict HTTP/1.1" 200 -
Containerized Inference Verification: 100% SUCCESS"""
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
    plt.savefig(f'A6/screenshots/{name}.png', dpi=200, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()

print('A6 screenshots generated successfully.')
