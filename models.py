from datetime import datetime
from typing import List
from pydantic import BaseModel, EmailStr

class Announcement(BaseModel):
    email_addresses: List[EmailStr]
    subject: str
    message: str
    send_time: datetime = datetime.now()
