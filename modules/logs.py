import logging
import os
import sys

def get_logger(level=10, name='debug'):
    """small method to create loggers with desired setup for module returns a logger. Logs to stdout as well as file
    
    Keyword Arguments:
        level {int} -- [logging level 10 : DEBUG, 20 : INFO, 30: WARNING, 40 : ERROR, 50 : CRITICAL] (default: {10})
        name {str} -- [name for the logger] (default: {'debug'})
    """    

    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] : %(message)s')
    logger_handler = logging.StreamHandler(sys.stdout)
    logger_handler.setFormatter(formatter)
    logger.addHandler(logger_handler)
    file_handler = logging.FileHandler(f'/home/{os.getlogin()}/monitor/logs/{name}-log.log')
    logger.addHandler(file_handler)
    
    return logger