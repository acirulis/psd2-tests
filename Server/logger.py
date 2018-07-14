import logging
import logging.handlers

LOG_LEVEL = logging.DEBUG
LOGGER_NAME = 'psd2'


def start_logger():
    # SET LOGGING #
    # https://docs.python.org/3/howto/logging.html#logging-levels
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(LOG_LEVEL)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(funcName)s:%(lineno)d - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    handler = logging.handlers.TimedRotatingFileHandler(filename='application.log', when='D', backupCount=5)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # if LOG_LEVEL == logging.DEBUG:
    #     consoleHandler = logging.StreamHandler()
    #     consoleHandler.setFormatter(formatter)
    #     logger.addHandler(consoleHandler)
    return logger


# try:
#     Logger
# except NameError:
#     Logger = start_logger()
#     Logger.info('Logger object initiated')

Logger = start_logger()
Logger.info('Logger object initiated')