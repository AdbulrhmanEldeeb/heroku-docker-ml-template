from pathlib import Path
import joblib
import numpy as np

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

# iris model
with open(f"{BASE_DIR}/trained_pipeline-{__version__}.joblib", "rb") as f:
    model = joblib.load(f)


classes = ["setosa", "versicolor", "virginica"]


def predict_pipeline(payload):

    input_values = np.array(
        [[payload.value1, payload.value2, payload.value3, payload.value4]],
        dtype=np.float16,
    )

    result = classes[int(model.predict(input_values)[0])]

    return result
