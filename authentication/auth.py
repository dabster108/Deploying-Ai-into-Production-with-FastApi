from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader
from collections import defaultdict

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



#lass RateLimiter:
    def __init__(self, request_per_min: int = 10):
        self.request_per_min = request_per_min
        self.requests = defaultdict(list)  # Corrected defaultdict usage

    def is_rate_limited(self, api_key: str) -> Tuple[bool, int]:  # Fixed indentation and type hint
        current_time = time.time()
        request_times = self.requests[api_key]


#rate_limiter = RateLimiter(Request_per_min = 10)