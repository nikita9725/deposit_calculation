import os
import sys
import logging
from logging import handlers

from settings import config


def get_logger(name):
    logger = logging.getLogger('app')
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s :: %(levelname)s :: %(filename)s.%(funcName)s %(message)s'
    )

    if not os.path.exists(config.log_path):
        os.makedirs(config.log_path)

    file_handler = handlers.RotatingFileHandler(config.log_path + '/app.log',
                                                'a', 1000000, 10)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    out_hdlr = logging.StreamHandler(sys.stdout)
    out_hdlr.setLevel(logging.DEBUG)
    out_hdlr.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(out_hdlr)

    return logging.getLogger('app.' + name)
