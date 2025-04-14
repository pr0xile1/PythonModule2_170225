my_list = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Исходный список: {my_list}")

# Сортировка по возрастанию (по умолчанию)
my_list.sort()
print(f"Сортировка по возрастанию: {my_list}")

# Сортировка по убыванию
my_list.sort(reverse=True)
print(f"Сортировка по убыванию: {my_list}")

# Сортировка списка строк по длине
words = ["яблоко", "банан", "вишня", "абрикос"]
words.sort(key=len)
print(f"Сортировка по длине слова: {words}")

# Сортировка списка кортежей по второму элементу
data = [(1, 5), (3, 2), (2, 8)]
data.sort(key=lambda item: item[1])
print(f"Сортировка по второму элементу кортежа: {data}")