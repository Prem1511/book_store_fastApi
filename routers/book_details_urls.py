# routers/book_details_urls.py

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials
from fastapi_dataclasses import *
from api_functions import *
from jwt_functions import verify_token

router = APIRouter()

@router.post("/create_book", tags=["Books"])
async def create_book_fun(item: CreateBookRequest, token: str = Depends(verify_token)):
    data=create_book(item)
    return data

@router.post("/get_book", tags=["Books"])
async def get_book_fun(item: GetBookRequest, token: str = Depends(verify_token)):
    data=get_book(item)
    return data

@router.post("/delete_book", tags=["Books"])
async def delete_book_fun(item: DeleteBookRequest, token: str = Depends(verify_token)):
    data=delete_book(item)
    return data
