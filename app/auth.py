from fastapi import Query, HTTPException, Depends
from app.config import API_KEY

def verify_api_key(api_key: str = Query(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return api_key