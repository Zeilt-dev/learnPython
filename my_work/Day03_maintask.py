# Научный калькулятор
import math

def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b

def divide(a: float, b: float) -> float:
    """Return a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(base: float, exp: float) -> float:
    """Return base raised to the power of exp."""
    return base ** exp

def square_root(n: float) -> float:
    """Return the square root of n. Raises ValueError if n < 0."""
    if n < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(n)

def main() -> None:
    """Run the interactive calculator."""
    operations = {
        "1": ("Сложение (+)", add, 2),
        "2": ("Вычитание (-)", subtract, 2),
        "3": ("Умножение (*)", multiply, 2),
        "4": ("Деление (/)", divide, 2),
        "5": ("Степень (^)", power, 2),
        "6": ("Корень (√)", square_root, 1),
    }

    print("=" * 40)
    print("       SCIENTIFIC CALCULATOR")
    print("=" * 40)

    while True:
        print("\nSelect operation:")
        for key, (name, _, _) in operations.items():
            print(f"  {key}. {name}")
        print("  q. Выход")

        choice = input("\nYour choice: ").strip().lower()

        if choice == "q":
            print("\nДо свидания!")
            break

        if choice not in operations:
            print("Неверный выюор, попробуйте снова")
            continue

        name, func, num_args = operations[choice]

        try:
            if num_args == 2:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = func(a, b)
                print(f"\nResult: {a} {name[name.index('(')+1]} {b} = {result}")
            else:
                a = float(input("Enter number: "))
                result = func(a)
                print(f"\nResult: {result:.6f}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()