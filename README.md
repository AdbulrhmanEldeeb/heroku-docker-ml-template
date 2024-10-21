# FastAPI ML Prediction API

This is a simple machine learning API built using FastAPI that serves predictions for the Iris dataset using a pre-trained model. The API is containerized using Docker for easy deployment.

## Project Structure

- `main.py`: Defines the FastAPI app, including endpoints for health check and prediction.
- `model/model.py`: Contains the code for loading the pre-trained model and making predictions.
- `model/trained_pipeline-0.1.0.joblib`: The serialized machine learning model used for prediction.
- `Dockerfile`: Configuration file for building the Docker image.
- `requirements.txt`: Lists the required Python dependencies.

## API Endpoints

- **GET `/`**: Health check endpoint. Returns the status of the API and the model version.
- **POST `/predict`**: Endpoint for making predictions. Accepts 4 numerical values as input and returns the predicted class (`setosa`, `versicolor`, or `virginica`).

### Example Request (POST `/predict`)
```json
{
    "value1": 5.1,
    "value2": 3.5,
    "value3": 1.4,
    "value4": 0.2
}
```
## Example Respone 
{
    "class_name": "setosa"
}

## Requirements
- Python 3.10+
- FastAPI
- Uvicorn
- Joblib
- NumPy

## Install dependencies via requirements.txt
```bash 
pip install -r requirements.txt
``` 

Running Locally
Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd docker_heroku_ml_template
Create and activate a virtual environment (optional but recommended):
```
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the dependencies:
```
```bash
pip install -r requirements.txt
Run the FastAPI app:
```
```bash
uvicorn app.main:app --reload
Access the API at http://127.0.0.1:8000.
```

## Docker Setup
Build the Docker image:

```bash
docker build -t my-ml-api .
Run the Docker container:
```
```bash
docker run -p 8000:8000 my-ml-api
Access the API at http://localhost:8000.
```
## Notes
The API serves predictions for the Iris dataset using a pre-trained model (trained_pipeline-0.1.0.joblib).

Ensure that you provide all 4 required values (as positive floats) in the POST /predict request.