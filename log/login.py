from fastapi import FastAPI
import logging
# setting up custom login 

logger = logging.getLogger(
    'uvicorn.error'
)

app = FastAPI()
logger.into("App is Running ")

@app.get('/')
async def main():
    logger.debug('GET /')
    return 'ok'