import logging
from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler
from os.path import join, pardir
from datetime import datetime


logs_manager = logging.getLogger(__name__)

def intitalize_logger() -> None:
    
    logs_format = "%(asctime)s — %(levelname)-7s — %(message)s" 
    logs_formatter = logging.Formatter(logs_format)


    stdout_handler = StreamHandler()
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(logs_formatter)

    logs_manager.setLevel(logging.DEBUG)

    file_handler = TimedRotatingFileHandler(
        filename=join('logs',"{}-logs.log".format(datetime.now().strftime("%d%m%Y"))),
        when='midnight',
        interval=1
    )
    
    file_handler.setFormatter(logs_formatter)
    logs_manager.addHandler(file_handler)
    logs_manager.addHandler(stdout_handler)