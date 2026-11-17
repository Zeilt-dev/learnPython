print("=====Исследование типов переменной=====")
print("Введите значение для определения типа.\n")
user_input = input("Введите значение: ")
print(f"Вы ввели: {user_input}")
print(f"type: {type(user_input).__name__}")
print()
print("--- Попытки преобразования ---")

# Попытка преобразоваия в "int"

try:
    as_int = int(user_input)
    print(f"Как int: {as_int}")
except ValueError:
    print("Как int: не возможно")

# Попытка преобразоваия в "float"

try:
    as_float = float(user_input)
    print(f"Как float: {as_float}")
except ValueError:
    print("Как float: не возможно")

# Всегда возможно преобразовать в строку

as_str = str(user_input)
print(f"Как string   : {as_str!r}")

# Логическая интерпретация

as_bool = bool(user_input)
print(f"bool: {as_bool}")
print()
print(f"Длина (в символах): {len(user_input)}")