from typing import Optional

from pydantic import BaseModel


# Shared properties
class Data(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
