# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.


num = int(input("Введите число: "))
result = 0

while num % 10 > 0:
    result = result if num % 10 <= result else num % 10
    num //= 10
else:
    print(result)
