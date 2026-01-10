import random
import string

def random_letters():
    while True:
        yield random.choice(string.ascii_lowercase) # в сі літери Англійського алфавіту

# приклад використання
gen = random_letters()

for i in range(15):
    print(next(gen))
