from datetime import datetime
from typing import List
from pydantic import BaseModel

class Announcement(BaseModel):
    phone_numbers: List[str]
    subject: str
    message: str
    send_time: datetime = datetime.now()
