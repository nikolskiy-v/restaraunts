from pydantic import BaseModel, ConfigDict

class MenuItemEntry(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str

class LinkItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = "created"
    menu_id: int
    items: list[MenuItemEntry]
