from pydantic import BaseModel

class Camp(BaseModel):
    camp_name: str
    location: str
    contact_no: int