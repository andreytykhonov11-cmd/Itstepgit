score = int(input("Вкажіть свою оцінку"))

if 0 <= score <= 49:
     print("Незадовільно")
elif 49 <= score <= 69:
     print("Задовільно")
elif 69 <= score <= 89:
     print("Добре")
elif 90 <= score <= 100:
     print("Відмінно")

else: print("error")

