import uuid
from fastapi import FastAPI

from models import Announcement
from services import send_announcement
import logging
from fastapi import HTTPException

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/health")
def health_check():
    return {"Hello": "World"}


@app.post("/anouncement/")
def create_anouncement(anouncement: Announcement, status_code=201):
    try:
        send_announcement(anouncement)
    except Exception as e:
        trace_id = uuid.uuid4()

        logger.error(f"{trace_id} - {e}")

        return HTTPException(status_code=500, detail=f"Could not send anouncement, please contact support for more details, trace ID: {trace_id}")


    return anouncement