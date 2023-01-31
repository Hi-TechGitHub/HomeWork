# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no
ticket = int(input("Your ticket is: "))

# last_operation = ticket // 10
# last_operation = last_operation % 10
# result = (ticket // 100) + (ticket % 10) + last_operation
first_three_numbers = ticket / 1000

last_operation1 = first_three_numbers // 10
last_operation1 = last_operation1 % 10
result1 = (ticket // 100) + (ticket % 10) + last_operation1

second_three_numbers = ticket % 1000
last_operation2 = second_three_numbers // 10
last_operation2 = last_operation2 % 10
result2 = (ticket // 100) + (ticket % 10) + last_operation2
if result1 == result2:
    print("Yes")
else:
    print("No")