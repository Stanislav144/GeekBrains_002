"""
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
📌 При создании нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков- архивов
📌 list-архивы также являются свойствами экземпляра
Добавьте строки документации и методы вывода информации на печать.
"""


class Archive:
    """
        Класс Archive хранит пару свойств (число и строку)
        и архивирует их в пару списков при создании каждого нового экземпляра

       Атрибуты:
           number (int): Числовое значение для хранения.
           string (str): Строковое значение для хранения.
           data_archive (list): Список, содержащий архивы предыдущих чисел и строк.

       Методы:
           add_to_archive(): Добавляет текущие значения числа и строки в архив.
           print_archive(): Выводит все данные из архива на печать.
           get_number(): Возвращает текущее числовое значение.
           get_string(): Возвращает текущее строковое значение.
       """

    def __init__(self, number, string):
        self.number = number
        self.string = string
        self.data_archive = []

    def add_to_archive(self):
        self.data_archive.append((self.number, self.string))

    def print_archive(self):
        print("Архив данных:")
        for data in self.data_archive:
            print(f"Число: {data[0]}, Строка: {data[1]}")

    def get_number(self):
        return self.number

    def get_string(self):
        return self.string

    @staticmethod
    def print_docstring():
        print(Archive.__doc__)


if __name__ == '__main__':
    Archive.print_docstring()
