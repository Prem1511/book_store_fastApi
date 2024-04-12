# fastapi_dataclass.py

from pydantic import BaseModel
from typing import Optional

class CreateBookRequest(BaseModel):
    book_name: Optional[str]=""
    description: Optional[str]=""
    number_of_pages: Optional[int]=""
    author_name: Optional[str]=""
    publisher_name: Optional[str]=""

class GetBookRequest(BaseModel):
    author_name: Optional[str]=""
    publisher_name: Optional[str]=""

class DeleteBookRequest(BaseModel):
    book_id: str
