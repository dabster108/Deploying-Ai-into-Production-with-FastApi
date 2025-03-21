import uvicorn
from script import app as script_app
from main import app as main_app

if __name__ == "__main__":
    uvicorn.run(main_app, host="0.0.0.0", port=8080)  # Choose which app to run
