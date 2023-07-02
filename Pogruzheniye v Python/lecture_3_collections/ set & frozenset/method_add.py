# Множество — набор уникальных неиндексированных элементов. В Python есть два вида множеств: set —
# изменяемое множество, frozenset — неизменяемое множество. Неизменяемое множество позволяет
# вычислять хеш и может использоваться там, где разрешён лишь хешированный тип данных,
# например в качестве ключа словаря.
my_set = {1, 2, 3, 4, 2, 5, 6, 7}
print(my_set)
my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,))
print(my_f_set)
# not_set = {1, 2, 3, 4, 2, 5, 6, 7, ['a', 'b']} # TypeError: unhashable type: 'list'
# Обратите внимание, что двойка передавалась в множества дважды, но хранится в единственном экземпляре,
# как один из уникальных элементов
# Метод add работает аналогично методу списка append, т.е. добавляет один элемент в коллекцию.
my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.add(9)
print(my_set)
my_set.add(7)
print(my_set)
# my_set.add(9, 10) # TypeError: set.add() takes exactly one argument (2 given)
my_set.add((9, 10))
print(my_set)
# Если попытаться добавить уже существующий элемент, множество не изменится.
# При попытке добавить несколько элементов получим ошибку TypeError.
