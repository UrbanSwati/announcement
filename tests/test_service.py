from models import Announcement
from datetime import datetime

from services import send_announcement

def test_sending_immedietly(mocker):
    send_to_whatsapp_fn = mocker.patch('services.send_to_whatsapp')

    send_to_whatsapp_fn.side_effect = lambda phone_numbers, message: print(phone_numbers, message)

    # Given an announcement with a send_time not set
    announcement = Announcement(
        phone_numbers=["12345"],
        subject="test",
        message="test",
    )

    # When send_announcement is called
    send_announcement(announcement)

    # Then send_to_whatsapp should be called with the announcement's phone numbers and message
    send_to_whatsapp_fn.assert_called_once_with(announcement.phone_numbers, announcement.message)

def test_sending_later(mocker):
    schedule_announcement_fn = mocker.patch('services.schedule_announcement')
    send_to_whatsapp_fn = mocker.patch('services.send_to_whatsapp')

    schedule_announcement_fn.side_effect = lambda announcement: print(announcement)

    # Given an announcement with a send_time set to a later stage
    announcement = Announcement(
        phone_numbers=["12345"],
        subject="test",
        message="test",
        send_time=datetime(2027, 3, 1, 0, 0, 0),
    )

    # When send_announcement is called
    send_announcement(announcement)

    # Then schedule_announcement should be called with the announcement
    schedule_announcement_fn.assert_called_once_with(announcement)

    # And send_to_whatsapp should not be called
    send_to_whatsapp_fn.assert_not_called()