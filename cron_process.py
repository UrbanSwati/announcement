import logging
from services import send_announcement

logger = logging.getLogger(__name__)

def cron_process(anouncement):
    """Process anouncement from cron job"""
    try:
        #TODO: have custom model for cronjob that has status and update anouncement status to sent
        send_announcement(anouncement)
    except Exception as e:
        logger.error(f"{e} - {anouncement}")