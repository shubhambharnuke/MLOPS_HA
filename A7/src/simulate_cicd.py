import subprocess
import sys

def simulate_pipeline(fail_scenario=False):
    print("="*60)
    print(f"Executing CI/CD Pipeline Simulation [Scenario: {'FAIL (Threshold 0.99)' if fail_scenario else 'PASS (Threshold 0.80)'}]")
    print("="*60)
    
    # Step 1: CI Build & Test
    print("[CI Job: Test ML Application] Starting on runner ubuntu-latest...")
    print("Step 1: Setting up Python 3.11 environment... DONE")
    print("Step 2: Installing dependencies (pytest, scikit-learn)... DONE")
    
    threshold = 0.99 if fail_scenario else 0.80
    accuracy = 0.9667
    print(f"Step 3: Running pytest test_model.py (Accuracy = {accuracy:.4f}, Threshold = {threshold})...")
    
    if accuracy >= threshold:
        print("  --> tests/test_model.py::test_model_accuracy PASSED [100%]")
        print("[CI Job: Test ML Application] Result: SUCCESS (exit code 0)")
        
        # Step 2: CD Deploy
        print("\n[CD Job: Deploy Application] Triggered (Condition: needs: test, branch: main)")
        print("Step 1: Checking out repository artifact... DONE")
        print("Step 2: Executing deployment simulation script:")
        print("  --> Deployment started...")
        print("  --> ML model deployed successfully to production staging.")
        print("[CD Job: Deploy Application] Result: SUCCESS")
        print("\nPipeline Result: ALL JOBS SUCCEEDED (Green Build)")
        return True
    else:
        print(f"  --> AssertionError: Model accuracy {accuracy:.4f} < required threshold {threshold}")
        print("  --> tests/test_model.py::test_model_accuracy FAILED [100%]")
        print("[CI Job: Test ML Application] Result: FAILED (exit code 1)")
        
        # Step 2: CD Deploy Skipped
        print("\n[CD Job: Deploy Application] SKIPPED (Condition 'needs: test' failed)")
        print("Pipeline Result: BUILD FAILED — Deployment Gating Blocked Untrusted Model.")
        return False

if __name__ == '__main__':
    print("--- Running Standard Pipeline (Passing) ---")
    simulate_pipeline(fail_scenario=False)
    print("\n\n--- Running Failing Pipeline (Failure Gating Demonstration) ---")
    simulate_pipeline(fail_scenario=True)
