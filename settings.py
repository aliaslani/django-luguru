# other imports
import os
from loguru import logger
from loguru_handler import LoguruHandler
import sys
from utils import LoguruHandler






BASE_DIR = ''



# other settings



LOG_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'loguru': {
            'class': 'loguru_handler.LoguruHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['loguru'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['loguru'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Add other loggers as needed
    },
}

# Configure Loguru
LOGURU_FORMAT = "{time} {level} {message}"
LOGURU_FILE_PATH = os.path.join(BASE_DIR, 'logs', 'django.log')

logger.remove()  # Remove the default handler
logger.add(LOGURU_FILE_PATH, format=LOGURU_FORMAT, level="DEBUG", rotation="10 MB", retention="1 week")  # File logging
logger.add(sys.stderr, format=LOGURU_FORMAT, level="ERROR")  # StdErr logging