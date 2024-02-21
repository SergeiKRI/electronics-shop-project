from src.item import Item


class Mixin:
    """Меняет раскладку EN -> RU -> EN"""

    __languauge = 'EN'

    @property
    def language(self) -> str:
        return self.__languauge

    def change_lang(self) -> None:
        if self.__languauge == "EN":
            self.__languauge = "RU"
        else:
            self.__languauge = 'EN'


class Keyboard(Item, Mixin):
    pass
