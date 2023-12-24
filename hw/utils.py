from datetime import datetime

from beer import Beer
from config import DATE_FORMAT
from wine import Wine


def str_to_date(converted_str: str) -> datetime.date:
    """Функция для конвертации строки в дату."""

    return datetime.strptime(converted_str, DATE_FORMAT).date()


def prepare_wines_test_data() -> list:
    """Полготовка тестовых объектов вин."""

    return [
        Wine(
            title='Пино Гриджио',
            production_date=str_to_date('25-05-2010')
        ),
        Wine(
            title='777',
            production_date=str_to_date('26-05-2010')
        ),
        Wine(
            title='Виноградный день',
            production_date=str_to_date('27-05-2010')
        ),
        Wine(title='Совиньон Блан'),
        Wine(production_date=str_to_date('28-05-2010')),
        Wine(),
    ]


def prepare_beer_test_data() -> list:
    """Полготовка тестовых объектов пива."""

    return [
        Beer(
            title='Аливария',
            production_date=str_to_date('25-05-2010')
        ),
        Beer(
            title='Козел Темный',
            production_date=str_to_date('26-05-2010')
        ),
        Beer(
            title='Guiness',
            production_date=str_to_date('27-05-2010')
        ),
        Beer(title='Старый мельник'),
        Beer(production_date=str_to_date('28-05-2010')),
        Beer(),
    ]
