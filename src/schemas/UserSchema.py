from datetime import date
from pydantic import BaseModel, Field
import uuid

class SchemaUser(BaseModel):

    id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    lastName: str = Field(min_length=1)
    username: str = Field(min_length=1)
    email: str = Field(min_length=1)
    password: str = Field(min_length=8)
    access: str = Field(default="user" ,min_length=1)
    
    def __init__(self, **data):
            if "id" not in data:
                data["id"] = uuid.uuid4().hex
            super().__init__(**data)
            
            