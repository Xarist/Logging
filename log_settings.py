LOG_SETTINGS = {
    'version': 1,
    'handlers': {
        'success_file_handler': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'success_responses.log',
            'formatter': 'detailed',
        },
        'bad_file_handler': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'bad_responses.log',
            'formatter': 'detailed',
        },
        'blocked_file_handler': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'blocked_responses.log',
            'formatter': 'detailed',
        },
    },
    'loggers': {
        'success_responses': {
            'handlers': ['success_file_handler'],
            'level': 'INFO',
            'propagate': False,
        },
        'bad_responses': {
            'handlers': ['bad_file_handler'],
            'level': 'WARNING',
            'propagate': False,
        },
        'blocked_responses': {
            'handlers': ['blocked_file_handler'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
    'formatters': {
        'detailed': {
            'format': '%(levelname)s: %(message)s'
        },
    },
}
