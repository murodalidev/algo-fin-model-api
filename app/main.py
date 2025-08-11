from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.auth import verify_api_key
from app.cache import cache
from app.sheets import get_google_sheet_data

app = FastAPI(title="Google Sheet API", version="1.0.0")    

ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS, 
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/sheet-data")
def sheet_data(
    head: str = Query(..., description="Boshlanish katak (masalan: A20)"),
    tail: str = Query(..., description="Tugash katak (masalan: B20)"),
    # _: str = Depends(verify_api_key),
):
    cache_key = f"worksheet_{head}_{tail}"
    if cache_key in cache:
        return {"rows": cache[cache_key]}

    try:
        data = get_google_sheet_data(head, tail)
        cache[cache_key] = data
        return {"rows": data}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})