import os 
import logging
from logging.config import dictConfig
from dotenv import load_dotenv

load_dotenv()

DISCORD_API_SECRET = os.getenv('DISCORD_TOKEN')

LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters":{
        "verbose":{
            "format": "(levelname)-10s - %(asctime)s - %(module) - 15s: %(message)s"
        },
        "standard":{
            "format": "(levelname)-10s - %(name) - 15s: %(message)s"
        }
    },
    "handlers":{
        "console":{
            'level': "DEBUG",
            'class': "logging.StreamHandler",
            'formatter': "standard"
        },
        "console2":{
            'level': "WARNING",
            'class': "logging.StreamHandler",
            'formatter': "standard"
        },
        "file":{
            'level': "INFO",
            'class': "logging.FileHandler",
            'filename': "logs/infos.log",
            'mode': "w",
            'formatter': "verbose"
        },
    },
    "Loggers":{
        "bot":{
            'handlers': ['console'],
            "level": "INFO",
            "propogate": False
        },
        "discord":{
            
            'handlers': ['console2', "file"],
            "level": "INFO",
            "propogate": False
        }
    }
    
}