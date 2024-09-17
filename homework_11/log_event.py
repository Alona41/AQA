import logging


def log_event(username, status):
    logger = logging.getLogger('event_logger')

    if status == 'success':
        logger.info(f"Login event - Username: {username}, Status: {status}")
    elif status == 'expired':
        logger.warning(f"Login event - Username: {username}, Status: {status}")
    elif status == 'failed':
        logger.error(f"Login event - Username: {username}, Status: {status}")