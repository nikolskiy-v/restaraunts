from pydantic import BaseModel
from datetime import datetime

class Base(BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    