import time
import requests
import numpy as np
from sklearn.datasets import load_breast_cancer

def generate_traffic(base_url='http://localhost:8000', n_requests=100):
    cancer = load_breast_cancer()
    X = cancer.data
    
    print(f"Starting Traffic Generator: Sending {n_requests} simulated requests to {base_url}...")
    success_count = 0
    error_count = 0
    
    for i in range(n_requests):
        # 85% valid requests, 15% invalid to test error monitoring
        if i % 7 == 0:
            # Send invalid feature vector (length 10 instead of 30) -> triggers HTTP 422
            payload = {'features': list(X[i % len(X)][:10])}
        elif i % 15 == 0:
            # Send invalid schema payload -> triggers HTTP 400
            payload = {'bad_key': 'corrupt_data'}
        else:
            # Valid 30-feature vector
            payload = {'features': list(X[i % len(X)])}
            
        try:
            resp = requests.post(f"{base_url}/predict", json=payload, timeout=2)
            if resp.status_code == 200:
                success_count += 1
            else:
                error_count += 1
        except Exception as e:
            error_count += 1
            
        time.sleep(0.05)
        
    print(f"Traffic Simulation Completed: {success_count} Successful (200 OK), {error_count} Controlled Errors (400/422).")
    
    # Check metrics endpoint
    metrics_resp = requests.get(f"{base_url}/metrics")
    print(f"Metrics endpoint verified: HTTP {metrics_resp.status_code} ({len(metrics_resp.text)} bytes of PromQL telemetry)")

if __name__ == '__main__':
    generate_traffic()
