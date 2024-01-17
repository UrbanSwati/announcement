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

    anouncement.phone_numbers = remove_duplicates(anouncement.phone_numbers)

    return anouncement