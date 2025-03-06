from pydantic import BaseModel
from typing import Optional, Any

class SuccessResponse(BaseModel):
    status: str = "success"
    message: str
    data: Optional[Any] = None
