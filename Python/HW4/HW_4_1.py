# Задача №1
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#     3. Валюту пользователя определите сами.

def exchanger(currency, currancy_rate):
    return currency * currancy_rate


amount = int(input())
print('Ты ввёл', amount, 'RUB')
print('конвертированная сумма в USD = ', round(exchanger(amount, 0.013), 2), 'USD')
