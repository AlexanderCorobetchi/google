s = input("Введите строку: ")

# Убираем все цифры и переворачиваем строку
result = ''.join(char for char in s if not char.isdigit())[::-1]

print("Результат:", result)