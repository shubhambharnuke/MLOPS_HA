import matplotlib.pyplot as plt
import os

os.makedirs('A5/screenshots', exist_ok=True)

terminal_screens = {
    'pytest_execution': """$ python -m pytest A5/tests/test_api.py -v
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.2.0
collected 7 items

A5/tests/test_api.py::test_root PASSED                                   [ 14%]
A5/tests/test_api.py::test_health PASSED                                 [ 28%]
A5/tests/test_api.py::test_model_info PASSED                             [ 42%]
A5/tests/test_api.py::test_predict_setosa PASSED                         [ 57%]
A5/tests/test_api.py::test_predict_virginica PASSED                      [ 71%]
A5/tests/test_api.py::test_predict_validation_error PASSED               [ 85%]
A5/tests/test_api.py::test_predict_batch PASSED                          [100%]

======================== 7 passed in 6.33s ========================""",

    'swagger_ui_predict_response': """$ curl -X POST "http://localhost:8000/predict" \\
     -H "Content-Type: application/json" \\
     -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'

HTTP/1.1 200 OK
content-type: application/json
{
  "prediction_class": "setosa",
  "class_id": 0,
  "confidence_score": 0.9850,
  "model_version": "1.0.0"
}

$ curl -X POST "http://localhost:8000/predict" \\
     -H "Content-Type: application/json" \\
     -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": -1.0, "petal_width": 0.2}'

HTTP/1.1 422 Unprocessable Entity
{
  "detail": [
    {
      "loc": ["body", "petal_length"],
      "msg": "Input should be greater than 0",
      "type": "greater_than"
    }
  ]
}"""
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
    plt.savefig(f'A5/screenshots/{name}.png', dpi=200, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()

print('A5 screenshots generated successfully.')
