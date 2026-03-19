from pydantic import BaseModel,Field
from typing import Optional,Any,Dict
from datetime import datetime,date

class User_schema(BaseModel):
    name: Optional[str] = None
    mail: Optional[str] = None
    age: Optional[int] = None
    create_by: Optional[str] = None
    create_date: Optional[datetime] = None

    class Config:
        orm_mode = True
