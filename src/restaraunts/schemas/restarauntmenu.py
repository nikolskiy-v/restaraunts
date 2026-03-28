from pydantic import BaseModel, ConfigDict

class RestaurantMenuEntry(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str

class LinkMenuResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = "created"
    restaraunt_id: int
    menus: list[RestaurantMenuEntry]
