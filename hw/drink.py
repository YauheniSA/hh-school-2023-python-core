class Drink:
    """Базовый клас для всех алкогольных напитков."""

    def __init__(self, title=None, production_date=None) -> None:
        self.title = title
        self.production_date = production_date

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return self.title
