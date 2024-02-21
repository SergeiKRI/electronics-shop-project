from src.item import Item

if __name__ == '__main__':
    # Файл item.csv отсутствует.
    Item.instantiate_from_csv('item.csv')
    # FileNotFoundError: Отсутствует файл items.csv

    # В файле item.csv удалена последняя колонка.
    Item.instantiate_from_csv('../src/item_bag.csv')
    # InstantiateCSVError: Файл items.csv поврежден
