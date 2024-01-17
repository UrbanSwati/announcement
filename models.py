from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class Announcement(BaseModel):
    phone_numbers: List[str]
    subject: str
    message: str
    send_time: Optional[datetime] = None
