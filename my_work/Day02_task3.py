# Строки
print("=" * 45)

text = "PYTHON"
print(text[0]) # P
print(text[5]) # N
print(text[-1]) # N
print(text[-4]) # T

print("=" * 45)

print(text[0:2]) # PY
print(text[:3]) # PYT
print(text[3:]) # HON
print(text[::-1]) # инверсия с конца
print(text[::2]) # каждая вторая буква начиная с P
print(text[::-2]) # каждая вторая буква начиная с N в обратном порядке
print(text[::-3]) # каждая третья буква начиная с N в обратном порядке

# Строковые методы
print("=" * 45)

name = "   Евгений андреевич Петров   "
print(name.upper()) # ЕВГЕНИЙ АНДРЕЕВИЧ ПЕТРОВ
print(name.lower()) # евгений андреевич петров
print(name.title()) # Евгений Андреевич Петров
print(name.strip()) # удаляет пробелы в начале и конце строки

print("=" * 45)

sent = "Я изучаю Python. Я хочу стать программистом."
print(sent.replace("Я", "I")) # заменяет все вхождения "Я" на "I"
print(sent.count("Я")) # считает количество вхождений "Я"
print(sent.find("Python")) # возвращает индекс первого вхождения "Python"
print(sent.find("Java")) # возвращает -1, если поиск неудачный
print(sent.split(".")) # разбивает строку на список по разделителю "."
print("".join(["Я", "изучаю", "Python"])) # объединяет список строк в одну строку с разделителем "."
print("".join(["one", "two", "three"]))

print("=" * 45)

email = "xxx@mail.ru"
print(email.startswith("user"))    # False
print(email.startswith("xxx"))     # True
print(email.endswith(".com"))      # False
print(email.endswith(".ru"))       # True
print(email.find("@"))             # 3

# f-строки
print("=" * 45)

name = "Eugene"
age = 30
hight = 180

print(f"Меня зовут {name}. Мне {age} лет. Мой рост {hight} см.")
print(f"Через 5 лет мне будет {age + 5} лет.")

# Форматирование чисел
print("=" * 45)

pi = 3.14159265
print(f"Pi до N числа: {pi:.2f}")            # В данном случае до второго знака после запятой с округлением
print(f"Pi до N числа: {pi:.4f}")            # В данном случае до четвертого знака после запятой с округлением
print(f"Pi до N числа: {pi:.5f}")            # В данном случае до пятого знака после запятой с округлением
print(f"Pi в процентах: {pi * 100:.1f}%")    # Типо проценты с округлением до одного знака после запятой
print(f"Pi в процентах: {pi * 100:.3f}%")    # Типо проценты с округлением до третьего знака после запятой
print(f"Pi в процентах: {pi * 100:.4f}%")    # Типо проценты с округлением до четвертого знака после запятой

# заполнение и выравнивание
print("=" * 45)

for i in range(1, 4):
    print(f"Item {i:>3}: {'*' * i}")