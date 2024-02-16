from datetime import date
from pydantic import BaseModel, Field
import uuid

class SchemaPost(BaseModel):

    id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    content: str = Field(min_length=1)
    summary: str = Field(min_length=1)
    publishedDate: date = Field(default=date.today())
    
    def __init__(self, **data):
            if "id" not in data:
                data["id"] = uuid.uuid4().hex
            super().__init__(**data)
            
