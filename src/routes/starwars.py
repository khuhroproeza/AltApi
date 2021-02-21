from fastapi import APIRouter
from typing import List


from src.controllers.data_loader import json_loader

router = APIRouter()


@router.get("/starwarscrafts", response_model=List[str])
def get_all_entities(descending: bool = False):
    aircraft_data = json_loader(descending)
    return aircraft_data