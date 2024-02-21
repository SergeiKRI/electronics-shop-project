import os

import pytest

from src.item import Item, InstantiateCSVError
from settings import NAME_BAG


def test_instantiate_from_csv_not_file():
    """
    Отсутствие файла
    """
    relative_path = "src/item1.csv"
    file_path = os.path.abspath(relative_path)
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(file_path)


def test_instantiate_from_csv_bad_file():
    """
    Поврежденный файл
    """
    file_path = os.path.abspath(NAME_BAG)
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(file_path)