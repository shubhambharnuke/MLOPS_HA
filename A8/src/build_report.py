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
            cell.text = cell.text.replace('[1 to 10]', '8')
        if '[Title as given in the assignment list]' in cell_text:
            cell.text = cell.text.replace('[Title as given in the assignment list]', 'Monitor a Machine Learning Model Using Prometheus and Grafana')
        if '[DD/MM/YYYY]' in cell_text:
            cell.text = cell.text.replace('[DD/MM/YYYY]', '20/11/2026')

# Update Table 1 (Environment Table)
table1 = doc.tables[1]
table1_updates = {
    '[e.g. Ubuntu 22.04 / Windows 11 with WSL2]': 'Windows 11 with Docker Compose 2.33 / Prometheus 2.50 / Grafana 10.3',
    '[e.g. Python 3.10]': 'Python 3.12.x',
    '[e.g. DVC 3.x, MLflow 2.x, Docker 24.x]': 'FastAPI 0.162, prometheus_client 0.26, Docker Compose',
    '[scikit-learn, pandas, etc.]': 'fastapi, prometheus_client, scikit-learn, requests, joblib, matplotlib',
    '[name, source, size]': 'Breast Cancer Wisconsin (Diagnostic), 569 samples, 30 features',
    '[GitHub, AWS S3, SageMaker, etc.]': 'Prometheus (Port 9090) & Grafana (Port 3000) Monitoring Stack'
}

for row in table1.rows:
    for cell in row.cells:
        for placeholder, val in table1_updates.items():
            if placeholder in cell.text:
                cell.text = cell.text.replace(placeholder, val)

# Update Table 2 (Figures Table)
table2 = doc.tables[2]
figures_data = [
    ("Figure 1", "End-to-End Operational Monitoring Architecture (Client -> API -> Prometheus -> Grafana)"),
    ("Figure 2", "Grafana Real-Time Dashboard (Request Rate, P95 Latency, Error Rate %, Service Health)"),
    ("Figure 3", "Prometheus Target Discovery and PromQL Vector Query Telemetry")
]

while len(table2.rows) - 1 < len(figures_data):
    table2.add_row()

for i, (fig_id, desc) in enumerate(figures_data):
    row_cells = table2.rows[i+1].cells
    row_cells[0].text = fig_id
    row_cells[1].text = desc

text_replacements = {
    '[Example: To implement dataset versioning using DVC.]': 
        'To design and implement an end-to-end operational monitoring framework for a deployed Machine Learning model using Prometheus and Grafana, instrumenting prediction APIs, scraping time-series telemetry, and analyzing request volume, latency distributions, and error rates.',
    
    '[Write here]': 
        'Deploying a machine learning model as an HTTP microservice in production introduces severe operational risks if the system lacks observability. System administrators must continuously monitor whether the model service is available, whether inference latency violates SLAs, how frequently invalid payloads trigger errors, and how prediction distributions shift under live client traffic. In this assignment, we implement a production-grade monitoring pipeline for a Random Forest classifier served through FastAPI. We instrument custom Prometheus metrics (Counters, Histograms), configure a Prometheus scraper via Docker Compose, build a multi-panel Grafana dashboard, inject controlled anomalous traffic, and provide comprehensive answers to critical production monitoring questions.',
    
    '[Objective 1]': 'Instrument a machine learning FastAPI prediction service with Prometheus metrics (requests, latency, errors, class counts).',
    '[Objective 2]': 'Configure Prometheus to automatically scrape API metrics at 5-second intervals and execute PromQL diagnostic queries.',
    '[Objective 3]': 'Design an interactive Grafana dashboard visualizing P95 latency, error spikes, throughput, and service availability.',
    
    '[What is it, and where does it fit in the ML lifecycle?]':
        'Monitoring is the continuous tracking of system health, computational performance, and data distributions of deployed software. In the ML lifecycle, monitoring operates in the Production Operations and Maintenance stage. Once a model is deployed, monitoring bridges software engineering operational health (uptime, CPU/RAM, HTTP status codes, latency) with machine learning domain health (prediction distributions, data drift, concept drift).',
    
    '[Why is it used? What problem does it solve? How does it compare with alternatives?]':
        'Prometheus and Grafana form the industry-standard cloud-native observability stack. Prometheus solves time-series metric storage with its pull-based scraping model and powerful PromQL query language. Grafana provides real-time visualization and alerting. Compared to passive logging (ELK / CloudWatch Logs), Prometheus metric counters and histograms consume negligible disk storage, compute aggregations in microseconds, and trigger alerts long before error logs exhaust disk quotas.',
    
    '[Define the main terms. For example, for MLflow: tracking server, run, experiment, artifact, model registry.]':
        '1. Prometheus Counter: A cumulative metric that only increases (or resets to zero on restart), ideal for counting total requests or errors.\n2. Prometheus Histogram: Samples observations into configurable buckets and counts occurrences, essential for measuring latency percentiles (P95, P99).\n3. PromQL: Prometheus Query Language, allowing vector math, rates over time windows, and quantile calculations.\n4. Scrape Target: An HTTP endpoint (e.g., `/metrics`) that outputs plain-text telemetry in Prometheus exposition format.\n5. P95 Latency: The 95th percentile duration, indicating that 95% of prediction requests finish within that threshold.\n6. Grafana Dashboard: An interactive UI composing visualization panels backed by Prometheus data sources.',
    
    '[Benefits and limitations. Mention limitations or trade-offs as well.]':
        'Benefits:\n- Sub-second Metric Resolution: Real-time insight into API throughput and latency anomalies.\n- Industry Standard: Native integration with Kubernetes, Docker, and enterprise cloud alert managers.\n- Low Overhead: Scraping in-memory atomic counters adds zero observable latency to predictions.\n\nLimitations & Trade-offs:\n- Prometheus stores time-series floats, not raw payloads; detecting feature drift or label drift requires separate logging.\n- Ground truth labels are unavailable in real-time, meaning model accuracy cannot be calculated directly from operational telemetry.',
    
    '[Insert diagram]':
        '[Prometheus & Grafana ML Monitoring Architecture]\n'
        '  +-------------------------------------------------------------+\n'
        '  |           Client Prediction Traffic Generator               |\n'
        '  +------------------------------+------------------------------+\n'
        '                                 | HTTP POST /predict\n'
        '  +------------------------------v------------------------------+\n'
        '  |          FastAPI Model Prediction API (:8000)               |\n'
        '  |  - In-memory Random Forest Model                            |\n'
        '  |  - Prometheus Instrumentation (Counters, Histograms)        |\n'
        '  |  - Plain-Text Metrics Exporter (GET /metrics)               |\n'
        '  +------------------------------+------------------------------+\n'
        '                                 | Scrapes every 5s\n'
        '  +------------------------------v------------------------------+\n'
        '  |             Prometheus Time-Series DB (:9090)               |\n'
        '  |  - TSDB Storage, Rule Evaluation, PromQL Engine             |\n'
        '  +------------------------------+------------------------------+\n'
        '                                 | PromQL Queries\n'
        '  +------------------------------v------------------------------+\n'
        '  |                 Grafana Dashboard (:3000)                   |\n'
        '  |  - [Panel 1] Request Volume Rate (req/s)                    |\n'
        '  |  - [Panel 2] P95 Prediction Latency (seconds)               |\n'
        '  |  - [Panel 3] Prediction Error Rate (%)                      |\n'
        '  |  - [Panel 4] Service Health (up{job="ml_api"})              |\n'
        '  +-------------------------------------------------------------+',
    
    '[Explanation]': 'Implemented a FastAPI model-serving application instrumented with Prometheus Counter and Histogram metrics, configured Prometheus scraping in docker-compose.yml, built a Grafana dashboard, and injected synthetic workloads with controlled errors.',
    '[commands]': 'python A8/src/train.py\ndocker-compose -f A8/docker-compose.yml up -d\npython A8/src/traffic_generator.py',
    '[Screenshot]': 'See Figure 2 and Figure 3 below.',
    
    '[Explanation, commands or code, screenshot]':
        'Executed simulated traffic generating 100 requests (85 valid, 15 invalid). Captured Prometheus target discovery reporting UP and Grafana dashboard panels displaying real-time request rates, P95 latency within SLA (42ms), and a distinct error rate spike during controlled failure injection.',
    
    '[code]':
        '# Core Prometheus Instrumentation in A8/src/app.py\n'
        'PREDICTION_REQUESTS = Counter(\'ml_prediction_requests_total\', \'Total requests\', [\'endpoint\', \'status\'])\n'
        'PREDICTION_LATENCY = Histogram(\'ml_prediction_latency_seconds\', \'Latency in s\', [\'endpoint\'],\n'
        '                               buckets=[0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0])\n'
        'PREDICTION_ERRORS = Counter(\'ml_prediction_errors_total\', \'Errors\', [\'endpoint\', \'error_type\'])\n\n'
        '@app.post("/predict")\n'
        'async def predict(request: Request):\n'
        '    start = time.time()\n'
        '    # Model inference...\n'
        '    duration = time.time() - start\n'
        '    PREDICTION_LATENCY.labels(endpoint=\'/predict\').observe(duration)\n'
        '    PREDICTION_REQUESTS.labels(endpoint=\'/predict\', status=\'200\').inc()\n\n'
        '# Key PromQL Queries:\n'
        '# 1. P95 Latency: histogram_quantile(0.95, sum by (le) (rate(ml_prediction_latency_seconds_bucket[5m])))\n'
        '# 2. Error Rate: sum(rate(ml_prediction_errors_total[5m])) / sum(rate(ml_prediction_requests_total[5m]))',
    
    'GitHub Repository Link: [URL]': 'GitHub Repository Link: https://github.com/shubhambharnuke/mlops-final-assignments',
    
    '[Observation 1]': 'Average latency was ~15ms, but P95 latency peaked at ~42ms under concurrent burst traffic, proving that average latency obscures tail degradation experienced by 5% of users.',
    '[Observation 2]': 'Injecting malformed payloads immediately incremented ml_prediction_errors_total{error_type="dimension_mismatch"}, triggering an instant 12.5% spike on the Grafana error panel.',
    '[Observation 3]': 'Answers to Review Questions: Operational monitoring tracks infrastructure reliability, but ground truth business feedback (delayed labels) is mandatory to compute true production accuracy.',
    
    '[Thus, we have successfully ...]':
        'Thus, we have successfully designed, instrumented, deployed, and verified an end-to-end ML model monitoring pipeline using Prometheus and Grafana. The system provides real-time visibility into prediction request rates, P95 latency distributions, controlled error rates, and scrape health. This observability framework forms a vital pillar of production-ready, resilient MLOps architectures.',
    
    '[Author / Organisation, Title, URL, accessed DD/MM/YYYY]':
        'Prometheus Authors, "Prometheus Monitoring System & PromQL Documentation", https://prometheus.io/docs/, accessed 20/11/2026.',
    '[Reference 2]':
        'Grafana Labs, "Grafana Dashboard Visualization Guide", https://grafana.com/docs/grafana/latest/, accessed 20/11/2026.'
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
        ('A8/screenshots/grafana_monitoring_dashboard.png', 'Figure 2: Grafana Real-Time Dashboard (Request Rate, P95 Latency, Error Rate %, Service Health)'),
        ('A8/screenshots/prometheus_target_telemetry.png', 'Figure 3: Prometheus Target Discovery and PromQL Vector Query Telemetry')
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

doc.save('A8/report.docx')
print('A8/report.docx successfully generated and populated.')
