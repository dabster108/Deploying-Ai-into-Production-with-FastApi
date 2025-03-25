import requests

# URL of the model file (Replace with a valid URL)
url = "https://raw.githubusercontent.com/coderlaviru/PENGUIN_MODEL_---/main/penguin_model.pkl"

# Local filename to save the model
filename = "penguin_classifier.pkl"

# Send GET request to download the file
response = requests.get(url, stream=True)

# Check if request was successful
if response.status_code == 200:
    with open(filename, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"Model downloaded successfully as {filename}")
else:
    print(f"Failed to download model. Status code: {response.status_code}")


''' Current Structure 
Request - > Validation - > Prediction -> Response Structure - > Client 
# Step 1: Request Model
class RequestModel(BaseModel):
    input_data: str

# Step 2: Validation
def validate_request(request: RequestModel):
    if not request.input_data:
        raise HTTPException(status_code=400, detail="Input data is required")
    return request.input_data

# Step 3: Prediction (Dummy Logic)
def make_prediction(data: str):
    return {"prediction": f"Processed: {data}"}

# Step 4: Response Structure
class ResponseModel(BaseModel):
    result: str

@app.post("/predict", response_model=ResponseModel)
def predict(request: RequestModel):
    validated_data = validate_request(request)
    prediction = make_prediction(validated_data)
    return ResponseModel(result=prediction["prediction"])

# Step 5: Client (Example cURL)
"""
curl -X 'POST' 'http://127.0.0.1:8000/predict' \
-H 'Content-Type: application/json' \
-d '{"input_data": "example"}'
"""

'''