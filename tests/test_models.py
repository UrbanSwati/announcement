from datetime import datetime
from models import Announcement

def test_announcement_model():

    raw_model = {
        "phone_numbers": ["12345", "123456", "123457"],
        "subject": "test",
        "message": "test",
        "send_time": "2021-03-01 00:00:00",
    }

    model = Announcement(**raw_model)

    assert model.phone_numbers == ["test@gmail.com", "test2@gmail.com", "test@gmail.com"]
    assert model.subject == "test"
    assert model.message == "test"
    assert model.send_time == datetime(2021, 3, 1, 0, 0, 0)

