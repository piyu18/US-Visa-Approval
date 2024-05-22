import logging
import os

from datetime import datetime
from from_root import from_root

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOG_DIR = 'logs'

LOG_PATH = os.path.join(from_root(), LOG_DIR, LOG_FILE)

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)