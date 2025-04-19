# Diabetes Prediction API

This repository contains a FastAPI-based application for predicting diabetes using machine learning models. The API provides endpoints to make predictions based on user input data.

## Features

- **FastAPI Framework**: High-performance API built with Python.
- **Machine Learning Integration**: Predicts diabetes using a pre-trained model.
- **JSON Input/Output**: Accepts input data in JSON format and returns predictions in JSON format.
- **Scalable and Lightweight**: Designed for production deployment.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/diabetes-api.git
    cd diabetes-api
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

2. Access the API documentation at:
    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

3. Use the `/predict` endpoint to make predictions by sending a POST request with the required input data.

## Input Data Format

The API expects input data in the following JSON format:
```json
{
  "age": 45,
  "bmi": 28.5,
  "glucose_level": 120,
  "blood_pressure": 80,
  "insulin": 85,
  "skin_thickness": 20
}
```

## Output

The API returns a JSON response indicating the prediction result:
```json
{
  "diabetes": true,
  "confidence": 0.85
}
```

## Deployment

To deploy the application in a production environment, use a production-ready ASGI server like `gunicorn` or `daphne`:
```bash
gunicorn -k uvicorn.workers.UvicornWorker main:app
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
