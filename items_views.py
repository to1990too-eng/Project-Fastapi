from typing import Annotated

from fastapi import APIRouter, Path

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]


@router.get("/latest")
def get_latest_item():
    return {"Item": {"id": "0", "name": "latest"}}


@router.get("/{item_id}")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=100000)]):
    return {
        "Item": {
            "id": item_id,
        },
    }