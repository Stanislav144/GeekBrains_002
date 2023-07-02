# Для проверки входит ли элемент в множество используют зарезервированное слово in.
my_set = {3, 4, 2, 5, 6, 1, 7}
print(42 in my_set)
# Внимание! Слово in позволяет сделать проверку на вхождение и в других коллекциях.
# Входит ли объект в list, tuple, является ли подстрока частью строки str, встречается ли ключ в словаре.
# Для list, tuple, str проверка на вхождение работает за линейное время O(n).
# Для dict, set, frozenset проверка работает за константное время O(1).
