"""
Создайте класс Моя Строка, где:
📌 будут доступны все возможности str
📌 дополнительно хранятся имя автора строки и время создания (time.time)
Добавьте строки документации и методы вывода информации на печать.
"""

import time


class MyString(str):
    """
    Класс MyString, унаследованный от str.

    Дополнительные атрибуты класса:
    - author: имя автора строки
    - created_time: время создания строки (time.time)
    """

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.author = "Unknown"
        instance.created_time = time.time()
        return instance

    def __init__(self, value, author=None):
        super().__init__()
        self.author = author or self.author

    def __str__(self):
        """
        Возвращает строковое представление объекта.

        Переопределенный метод str().
        """
        return super().__str__()

    def __repr__(self):
        """
        Возвращает строковое представление объекта для отладки.

        Переопределение встроенной функции repr().
        """
        return f"MyString('{str(self)}', author='{self.author}')"

    def print_info(self):
        """Вывод информации о строке на печать."""
        print("Строка:", str(self))
        print("Автор:", self.author)
        print("Время создания:", self.created_time)

    @staticmethod
    def print_docstring():
        """Вывод документации класса на печать."""
        print(MyString.__doc__)


s = MyString("Привет, мир!", author="John Doe")
s.print_info()
print(repr(s))
MyString.print_docstring()
