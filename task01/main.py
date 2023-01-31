# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
a = 0
result = 0
number = int(input("Enter number: "))



last_operation = number // 10
last_operation = last_operation % 10
result = (number // 100) + (number % 10) + last_operation
print(result)