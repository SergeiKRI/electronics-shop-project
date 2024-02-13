import pytest

from src.item import Item
@pytest.fixture
def constant():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    item = Item('Телефон', 10000, 5)
    return item1, item2, item
def test_positive_init(constant):
    item1 = constant[0]
    item2 = constant[1]
    assert item1.calculate_total_price == 200000
    assert item2.calculate_total_price == 100000
def test_apply_discount(constant):
    item1 = constant[0]
    item2 = constant[1]
    # устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # применяем скидку
    item1.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 20000

def test_name(constant):
    item = constant[2]
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'

def test_instantiate_from_csv():
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
def test_repr_str(constant):
    item1 = constant[0]
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'