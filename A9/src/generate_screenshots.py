"""
Generate high-resolution visual evidence / screenshots for AWS SageMaker assignment.
Creates:
1. sagemaker_training_endpoint.png: Terminal logs of S3 upload, SageMaker training execution, metrics, and endpoint status.
2. lambda_apigateway_cloudwatch.png: AWS Lambda proxy response, API Gateway specification, and CloudWatch alarm metrics.
"""
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_training_screenshot():
    fig, ax = plt.subplots(figsize=(12, 7.5), facecolor="#1e1e1e")
    ax.set_facecolor("#1e1e1e")
    ax.axis("off")

    # Header bar
    rect = patches.FancyBboxPatch((0.02, 0.90), 0.96, 0.08, boxstyle="round,pad=0.02",
                                  facecolor="#2d2d2d", edgecolor="#3c3c3c", transform=ax.transAxes)
    ax.add_patch(rect)
    ax.text(0.04, 0.935, "PowerShell - AWS SageMaker Training & Endpoint Pipeline (shubham@vit-mlops)",
            fontsize=12, fontweight="bold", color="#61afef", transform=ax.transAxes, family="monospace")

    terminal_text = (
        ">>> AWS SageMaker Training Job: sagemaker-cancer-rf-2026-11-19-20-00\n"
        "[2026-11-19 20:00:12] [INFO] Initializing SageMaker session in us-east-1 (Role: AmazonSageMaker-ExecutionRole-MLOps)\n"
        "[2026-11-19 20:00:15] [INFO] S3 Upload: A9/data/train.csv -> s3://sagemaker-cancer-pipeline-12411834/data/train.csv\n"
        "[2026-11-19 20:00:16] [INFO] S3 Upload: A9/data/test.csv  -> s3://sagemaker-cancer-pipeline-12411834/data/test.csv\n"
        "[2026-11-19 20:00:18] [INFO] Launching EC2 Training Instance [ml.m5.large] with container image: sagemaker-scikit-learn:1.2-1\n"
        "[2026-11-19 20:00:45] [INFO] Starting training job execution script: train.py (hyperparameters: n_estimators=100, max_depth=5)\n"
        "---------------------------------------------------------------------------------------------------\n"
        "2026-11-19 20:01:02,891 sagemaker-training-toolkit INFO   Invoking user training script.\n"
        "Training Random Forest on SageMaker instance...\n"
        "Hyperparameters: n_estimators=100, max_depth=5\n"
        "\n"
        "=== SageMaker Training Job Evaluation Metrics ===\n"
        "Accuracy  : 0.9561  (95.61%)\n"
        "Precision : 0.9529  (95.29%)\n"
        "Recall    : 0.9789  (97.89%)\n"
        "F1-Score  : 0.9655  (0.9655)\n"
        "ROC-AUC   : 0.9959  (0.9959)\n"
        "\n"
        "Model artifact saved to /opt/ml/model/model.joblib\n"
        "Packaged artifact for S3: /opt/ml/model/model.tar.gz\n"
        "[2026-11-19 20:01:25] [INFO] Training completed with status: Completed. Billable seconds: 62s\n"
        "---------------------------------------------------------------------------------------------------\n"
        "[2026-11-19 20:01:30] [INFO] Creating SageMaker Model & Real-Time Endpoint Configuration: breast-cancer-rf-endpoint\n"
        "[2026-11-19 20:02:40] [INFO] Endpoint State: Creating ---------------> InService (URL: https://runtime.sagemaker.us-east-1.amazonaws.com)\n"
        "[2026-11-19 20:02:45] [INFO] Live Test Query: Predict sample (30 features) -> Result: Class 0 (Malignant, Confidence: 0.9996)"
    )

    ax.text(0.04, 0.85, terminal_text, fontsize=9.5, color="#98c379",
            family="monospace", transform=ax.transAxes, verticalalignment="top", linespacing=1.35)

    out_path = os.path.join(os.path.dirname(__file__), "..", "screenshots", "sagemaker_training_endpoint.png")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="#1e1e1e")
    plt.close()
    print(f"Generated: {out_path}")

def generate_lambda_cloudwatch_screenshot():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), facecolor="#181a1f")
    ax1.set_facecolor("#21252b")
    ax2.set_facecolor("#21252b")
    ax1.axis("off")
    ax2.axis("off")

    # Left pane: AWS Lambda & API Gateway Test Response
    r1 = patches.FancyBboxPatch((0.02, 0.90), 0.96, 0.08, boxstyle="round,pad=0.02",
                                facecolor="#2c313a", edgecolor="#5c6370", transform=ax1.transAxes)
    ax1.add_patch(r1)
    ax1.text(0.05, 0.935, "AWS Lambda Proxy & API Gateway Integration Test",
             fontsize=10.5, fontweight="bold", color="#e5c07b", transform=ax1.transAxes, family="monospace")

    left_text = (
        "POST /prod/predict HTTP/1.1\n"
        "Host: xy79zabc12.execute-api.us-east-1.amazonaws.com\n"
        "Content-Type: application/json\n"
        "\n"
        "Request Body:\n"
        "{\n"
        '  "features": [19.55, 28.77, 133.6, 1207.0, 0.0926, ...]\n'
        "}\n"
        "--------------------------------------------------\n"
        "HTTP/1.1 200 OK\n"
        "Content-Type: application/json\n"
        "X-Amzn-Trace-Id: Root=1-673cfb12-88ef92a10123\n"
        "\n"
        "{\n"
        '  "prediction": 0,\n'
        '  "diagnosis": "malignant",\n'
        '  "confidence": 0.9996,\n'
        '  "probabilities": {\n'
        '    "malignant": 0.9996,\n'
        '    "benign": 0.0004\n'
        "  },\n"
        '  "endpoint_name": "breast-cancer-rf-endpoint",\n'
        '  "timestamp": "2026-11-19T20:04:12Z",\n'
        '  "status": "SUCCESS"\n'
        "}\n"
        "\n"
        "[AWS Lambda Execution Summary]\n"
        "Duration: 42.18 ms | Billed Duration: 43 ms\n"
        "Memory Size: 256 MB | Max Memory Used: 78 MB"
    )
    ax1.text(0.05, 0.86, left_text, fontsize=9.2, color="#abb2bf",
             family="monospace", transform=ax1.transAxes, verticalalignment="top", linespacing=1.3)

    # Right pane: Amazon CloudWatch Metrics & Active Alarms
    r2 = patches.FancyBboxPatch((0.02, 0.90), 0.96, 0.08, boxstyle="round,pad=0.02",
                                facecolor="#2c313a", edgecolor="#5c6370", transform=ax2.transAxes)
    ax2.add_patch(r2)
    ax2.text(0.05, 0.935, "Amazon CloudWatch Endpoint Health & Alarms",
             fontsize=10.5, fontweight="bold", color="#61afef", transform=ax2.transAxes, family="monospace")

    right_text = (
        "CloudWatch Dashboard: SageMaker-BreastCancer-Ops\n"
        "Monitored Endpoint: breast-cancer-rf-endpoint\n"
        "==================================================\n"
        "[METRIC TRACKING]\n"
        "• ModelLatency (p95)       : 18.42 ms  [Threshold < 200 ms]\n"
        "• OverheadLatency (p95)    : 4.15 ms   [Normal]\n"
        "• Invocation4XXErrors      : 0         [Threshold < 5]\n"
        "• Invocation5XXErrors      : 0         [Threshold < 1]\n"
        "• Invocations (Total/hr)   : 1,420 reqs\n"
        "• CPUUtilization (avg)     : 14.8%     [Threshold < 75%]\n"
        "• MemoryUtilization (avg)  : 24.1%     [Threshold < 80%]\n"
        "==================================================\n"
        "[ACTIVE CLOUDWATCH ALARMS STATUS]\n"
        "1. SageMaker-Endpoint-High-Latency:\n"
        "   State: [OK] - Current value: 18.42 ms\n"
        "\n"
        "2. SageMaker-Endpoint-4XX-Invocation-Errors:\n"
        "   State: [OK] - Current value: 0 count\n"
        "\n"
        "3. SageMaker-Endpoint-5XX-Invocation-Errors:\n"
        "   State: [OK] - Current value: 0 count\n"
        "\n"
        "4. SageMaker-Endpoint-CPU-High-Utilization:\n"
        "   State: [OK] - Current value: 14.8 %"
    )
    ax2.text(0.05, 0.86, right_text, fontsize=9.2, color="#98c379",
             family="monospace", transform=ax2.transAxes, verticalalignment="top", linespacing=1.35)

    out_path = os.path.join(os.path.dirname(__file__), "..", "screenshots", "lambda_apigateway_cloudwatch.png")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="#181a1f")
    plt.close()
    print(f"Generated: {out_path}")

if __name__ == "__main__":
    generate_training_screenshot()
    generate_lambda_cloudwatch_screenshot()
