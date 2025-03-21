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
