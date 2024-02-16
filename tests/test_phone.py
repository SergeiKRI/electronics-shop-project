import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def constant():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)

    return phone, item1


def test_str_repr(constant):
    phone = constant[0]
    assert str(phone) == 'iPhone 14'
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_add(constant):
    phone = constant[0]
    item = constant[1]
    assert item + phone == 25
    assert phone + phone == 10
    # assert phone + 10 == "Не является экземпляром Phone или Item классов"


def test_sim_is_int(constant):
    phone = constant[0]
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3
    phone.number_of_sim = 0.2
    assert phone.number_of_sim == 3


