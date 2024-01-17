from models import Announcement
from datetime import datetime

from services import send_announcement

def test_sending_immedietly(mocker):
    send_to_whatsapp_fn = mocker.patch('services.send_to_whatsapp')

    send_to_whatsapp_fn.side_effect = lambda phone_numbers, message: print(phone_numbers, message)

    # Given an announcement with a send_time not sent
    announcement = Announcement(
        phone_numbers=["12345"],
        subject="test",
        message="test",
    )

    # When send_announcement is called
    send_announcement(announcement)

    # Then send_to_whatsapp should be called with the announcement's phone numbers and message
    send_to_whatsapp_fn.assert_called_once_with(announcement.phone_numbers, announcement.message)