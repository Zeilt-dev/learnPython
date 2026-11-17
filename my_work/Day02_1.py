# Ввод переменных

name = "Eugene"
age = 30
rost = 179.
student = False

# Вывод переменных
print("=" * 45)

print(name)
print(age)
print(age + 2)
print(student)

# Проверка и преобразование типов
print("=" * 45)

x = 101
y = 2.5

print(type(x))
print(type(y))
print(type(name))
print(type(student))
print(x + y)
print(type(x + y))
print(x + int(y))
print(y + float(x))
print(type(x + int(y)))
print(type(y + float(x)))

# Преобразование типов
print("=" * 45)

x = "10"
int_x = int(x)
print(int_x)
print(type(x))
print(type(int_x))

float_x = float(x)
float_X2 = float(int_x)
print(float_x)
print(float_X2)
print(type(float_x))
print(type(float_X2))

# Преобразование в строку
print("=" * 45)

a = str(int_x)
b = str(float_x)
print(a)
print(b)
print(type(a))
print(type(b))

# Множественное присваивание
print("=" * 45)

q, w, e = 1, 2, 3
print(q, w, e)

p = o = i = 5
print(p, o, i)

# Переприсваивание переменных
print("=" * 45)

q , w = w , q
print(q, w)