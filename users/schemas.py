from pydantic import BaseModel, EmailStr, Field
from typing import Annotated
from annotated_types import MinLen, MaxLen

class CreateUser(BaseModel):
    # username: str = Field(..., max_length=20, min_length=3)
    username: Annotated[str, MaxLen(20), MinLen(3)]
    email: EmailStr

