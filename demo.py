from us_visa.logger import logging
from us_visa.exception import CustomException
import sys

try:
    1/0
except Exception as e:
    logging.info(e)
    raise CustomException(e,sys)