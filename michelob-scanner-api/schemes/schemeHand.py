from pydantic import BaseModel
from typing import Optional

class Hand(BaseModel):
    id_User: Optional[int] = None
    image: str
    token: str