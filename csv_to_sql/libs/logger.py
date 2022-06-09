import logging

LOG_LEVEL_BY_NAME = {
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG,
}

def get_instance(name: str="csv_to_sql") -> logging.Logger:
    """
    Args:
        name (str, optional): Name of the shared logger. Defaults to "csv_to_sql".
    Returns:
        logging.Logger
    """
    logger = logging.getLogger(name)
    logger.handlers = []
    formatter = logging.Formatter(fmt='[%(levelname)s] [%(filename)s:%(funcName)s:%(lineno)d] %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
