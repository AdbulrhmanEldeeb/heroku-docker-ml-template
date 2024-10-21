# # Use the official Python image from Docker Hub
# FROM python:3.10-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements.txt (if you have one) and install the dependencies
# # If you don't have a requirements file, you can skip this step or create one
# COPY requirements.txt .

# # Install dependencies
# RUN pip install --no-cache-dir --upgrade pip && \
#     pip install --no-cache-dir -r requirements.txt

# # Copy the entire app directory to the container
# COPY ./app ./app

# # Expose the port on which heroku will run fastapi 
# EXPOSE ${PORT}

# # Set environment variables
# # ENV PYTHONUNBUFFERED=1

# # Run FastAPI app using Uvicorn
# # CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "${PORT}"]


FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app