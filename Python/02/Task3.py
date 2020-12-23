# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.


month_number = int(input("Введите номер месяца: "))

# через список
seasons_list = ["Зима", "Весна", "Лето", "Осень"]

print(month_number, "месяц относится к сезону", seasons_list[month_number // 3 % 4])

# через словарь
seasons_dict = {0: "Зима", 1: "Весна", 2: "Лето", 3: "Осень"}

print(month_number, "месяц относится к сезону", seasons_dict[month_number // 3 % 4])