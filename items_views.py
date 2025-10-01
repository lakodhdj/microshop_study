from fastapi import Path, APIRouter 

from typing import Annotated


router = APIRouter(prefix = "/items",tags=["items"])


@router.get("/")
def items():
    return [
        "i1", "i2", "i3", "i4"
    ]

@router.get("{item_id}")
def items_id(item_id: Annotated[int, Path(ge=1, lt = 1_000_000)]):
    return {
        "item": {
            "id" : item_id + 12
        }
    }
    