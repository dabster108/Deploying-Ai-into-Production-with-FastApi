from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader

auth = FastAPI()

header_scheme = APIKeyHeader(
    name="API-KEY",
    auto_error=None
)

API_SECRET_KEY = "SECRET-KEY"

# Authenticating the endpoint 
@auth.get("/items")
def read_items(api_key: str = Depends(header_scheme)):
    if api_key is None or api_key != API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid or missing API key")
    
    return {"message": "Access granted", "items": ["item1", "item2", "item3"]}
