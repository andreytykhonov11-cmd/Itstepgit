a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
op = input("Введіть дію (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Ділення на нуль!")
    else:
        print(a / b)
else:
    print("Невідома операція!")