from typing import List, Union

from fastapi import FastAPI

from models import Announcement

from utils import remove_duplicates

app = FastAPI()

@app.get("/health")
def read_root():
    return {"Hello": "World"}


@app.post("/anouncement/")
def read_item(anouncement: Announcement):

    anouncement.email_addresses = remove_duplicates(anouncement.email_addresses)

    return anouncement