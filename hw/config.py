import functools
import logging
import time


DATE_FORMAT = '%d-%m-%Y'
LOGGING_DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
LOGGING_MESSAGE_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'


logging.basicConfig(
    datefmt=LOGGING_DATETIME_FORMAT,
    format=LOGGING_MESSAGE_FORMAT,
    level=logging.INFO,
    handlers=(logging.StreamHandler(),)
)


def logging_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'Функция {func.__name__} начала выполнение.')
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(
            f'Вермя выполнения функции {end_time - start_time} секунд.'
        )
        return result
    return wrapper
