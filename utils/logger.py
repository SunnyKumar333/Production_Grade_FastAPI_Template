import logging
from logging.handlers import RotatingFileHandler
from pythonjsonlogger import jsonlogger
from utils.context import corelationIDContextVar
from utils.generate_corelation_id import generateCorrelationID
from configs import config
from pathlib import Path


setting=config.get_settings()
LOG_DIR = Path(setting.log_dir)
LOG_DIR.mkdir(exist_ok=True)

class CorrelationFilter(logging.Filter):
    def filter(self, record):
        record.correlation_id = corelationIDContextVar.get()
        return True

def setupLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()#log to file
   
    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s %(correlation_id)s"
    )
    console_handler.setFormatter(formatter)
    
    # file handler 
    file_handler = RotatingFileHandler(
        f"{LOG_DIR}/app.log",
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=5              # keep 5 old files
    )
    file_handler.setFormatter(formatter)
    
    # adding filter to both handlers
    console_handler.addFilter(CorrelationFilter())
    file_handler.addFilter(CorrelationFilter())

    logger.addHandler(console_handler)
    # logger.addHandler(file_handler)

    return logger

logger=setupLogger()

