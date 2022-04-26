from function import get_greater_roman

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class Request(BaseModel):
	text: str


@router.post("/search")
def search(request: Request):
    text = request.text
    return get_greater_roman(text)