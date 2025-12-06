import random
secret = random.randint(1, 10)
attempts = 3
for i in range(attempts):
    guess = int(input("Вгадай число від 1 до 10: "))

    if guess == secret:
        print("Молодець! Ти вгадав!")
        break
    elif guess > secret:
        print("Менше!")
    else:
        print("Більше!")

if guess != secret:
    print(f"Ти програв! Загадане число було {secret}")
