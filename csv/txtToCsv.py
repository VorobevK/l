import random
import csv
from transliterate import translit

txt_file_path = "students.txt"
with open(txt_file_path, "r") as txt_file:
    lines = txt_file.readlines()


csv_data = []
for line in lines:
    full_name = line.strip()
    last_name, first_name, middle_name = full_name.split(maxsplit=2)
    username = f"{first_name[0]}{last_name}2024"
    username_english = translit(username, 'ru', reversed=True)
    password = random.randint(1000, 9999)
    email = f"{username_english}@Gmail.com"
    city = random.choice(["Минск", "Гомель", "Могилев", "Гродно", "Витебск", "Брест"])
    subject = "КСИС"
    group = "ПМС"
    course = 3
    csv_data.append([username_english, password, last_name, first_name, middle_name, email, city, subject, group, course])


csv_file_path = "students.csv"
with open(csv_file_path, "w", newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter=";")
    writer.writerow(["Username", "Пароль", "Фамилия", "Имя", "Отчество", "Email", "Город", "Изучаемый предмет", "Группа", "Курс"])
    for row in csv_data:
        writer.writerow(row)

print(f"CSV файл успешно создан: {csv_file_path}")
