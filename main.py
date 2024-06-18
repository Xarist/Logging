import requests as rq
import logging.config
from log_settings import LOG_SETTINGS

logging.config.dictConfig(LOG_SETTINGS)
success_logger = logging.getLogger('success_responses')
bad_logger = logging.getLogger('bad_responses')
blocked_logger = logging.getLogger('blocked_responses')

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            success_logger.info(f'{site}, response - {response.status_code}')
        else:
            bad_logger.warning(f'{site}, response - {response.status_code}')
    except rq.exceptions.Timeout:
        blocked_logger.error(f"'{site}', NO CONNECTION")
    except rq.exceptions.RequestException as e:
        blocked_logger.error(f"'{site}', NO CONNECTION")
