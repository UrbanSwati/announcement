from typing import List
from models import Announcement
from utils import remove_duplicates
from datetime import datetime

def send_to_whatsapp(phone_number: List[str], message: str):
    """Send message to whatsapp phone numbers"""
    #TODO: update reciepent status to sent in db, perhaps retry if failed to send to specific number
    pass

def send_announcement(announcement: Announcement):
    """Send announcement to whatsapp phone numbers"""
    try:
        if announcement.send_time and announcement.send_time > datetime.now():
            schedule_announcement(announcement)
            return

        announcement.phone_numbers = remove_duplicates(announcement.phone_numbers)
        send_to_whatsapp(announcement.phone_numbers, announcement.message)
    except Exception as e:
        raise e

def schedule_announcement(announcement: Announcement):
    """Schedule announcement"""
    pass