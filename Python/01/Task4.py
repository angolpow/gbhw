# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.


num = int(input("Введите число: "))
result = 0

while num:
    result = result if num % 10 <= result else num % 10
    num //= 10

print(result)
