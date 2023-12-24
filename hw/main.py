from market import Market
from utils import (
    prepare_wines_test_data, prepare_beer_test_data, str_to_date
)


def main() -> None:
    """Основаная логика приложения."""

    market = Market(
        beers=prepare_beer_test_data(),
        wines=prepare_wines_test_data()
    )

    # Task 1. Получение списка всех напитков, отсортированных по наименованию
    sorted_drinks = market.get_drinks_sorted_by_title()
    print(f'\nНапитки отсортированные по наименованию:\n {sorted_drinks}\n')

    # Task 2. Проверка наличия напитка по наименованию
    # в магазине есть 'Guiness' но нет 'Каберне'
    assert market.has_drink_with_title('Guiness') is True
    assert market.has_drink_with_title('Каберне') is False

    # пустой запрос вернет False
    assert market.has_drink_with_title() is False
    # None вернет False
    assert market.has_drink_with_title(None) is False

    # Task 3. Получение списка объектов напитка с указанным диапозоном дат.
    # Вариант 1. Переданы обе даты для фильтрации
    drinks_by_production_date = market.get_drinks_by_production_date(
        from_date=str_to_date('24-05-2010'),
        to_date=str_to_date('25-05-2010')
    )
    print('\n--Когда переданы обе даты для фильтрации--')
    for drink in drinks_by_production_date:
        print(f'{drink.title}, date: {drink.production_date}')

    # Вариант 2. Передана только from_date
    drinks_by_production_date = market.get_drinks_by_production_date(
        from_date=str_to_date('26-05-2010')
    )
    print('\n--Передана только from_date=26-05-2010--')
    for drink in drinks_by_production_date:
        print(f'{drink.title}, date: {drink.production_date}')

    # Вариант 3. Передана только to_date
    drinks_by_production_date = market.get_drinks_by_production_date(
        to_date=str_to_date('25-05-2010')
    )
    print('\n--Передана только to_date=25-05-2010--')
    for drink in drinks_by_production_date:
        print(f'{drink.title}, date: {drink.production_date}')

    # Вариант 2. Не передано ничего
    drinks_by_production_date = market.get_drinks_by_production_date()
    print('\n--Не передано ничего--')
    for drink in drinks_by_production_date:
        print(f'{drink.title}, date: {drink.production_date}')


if __name__ == '__main__':
    main()
