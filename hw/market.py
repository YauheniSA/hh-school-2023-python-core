from config import logging_decorator


class Market:
    """Класс для алкомагазина."""

    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = {wine.title: wine for wine in wines if wine.title}
        self.beers = {beer.title: beer for beer in beers if beer.title}

    @logging_decorator
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        return title in self.wines | self.beers

    @logging_decorator
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        return sorted(
            (self.wines | self.beers).values(), key=lambda drink: drink.title
        )

    @logging_decorator
    def get_drinks_by_production_date(
            self, from_date=None, to_date=None
            ) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date
        по to_date

        :return: list
        """

        return filter(
            self.get_filtering_func(from_date, to_date),
            [
                drink for drink in (self.wines | self.beers).values() if (
                    drink.production_date
                )
            ]
        )

    @staticmethod
    def get_filtering_func(from_date, to_date):
        """Функция для получения параметров фильтрации."""

        if from_date is None and to_date is None:
            return None

        if from_date is None and to_date:
            return lambda x: x.production_date <= to_date

        if from_date and to_date is None:
            return lambda x: x.production_date >= from_date

        return lambda x: from_date <= x.production_date <= to_date
