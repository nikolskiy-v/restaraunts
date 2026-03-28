from pydantic import BaseModel

class RestaurantMenuEntry(BaseModel):
    id: int
    name: str

class LinkMenuResponse(BaseModel):
    status: str = "created"
    restaraunt_id: int
    menus: list[RestaurantMenuEntry]
