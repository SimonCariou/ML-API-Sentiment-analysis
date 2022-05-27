from fastapi import FastAPI, HTTPException, Request, status, Depends
from fastapi.responses import JSONResponse

from auth.auth_rules import get_auth_status, get_admin_auth_status

#from pydantic import BaseModel
#from typing import Optional, List

responses = {
    200: {"message": "OK"},
    404: {"message": "Item not found"},
    302: {"message": "The item was moved"},
    403: {"message": "Not enough privileges"}
}

api = FastAPI(
    title='ML API - Sentiment Analysis',
    description="Gives a score to a text review. The score ranges from 1 to 5; 1 being the most negative.",
    version="1.0.0"
)


@api.get("/", responses = responses, name = "Check if the API is running")
async def get_root(isAdmin: bool = Depends(get_admin_auth_status)):
    return {"Status": "The API is running"}