# Задача №3
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#                 "конвертированная сумма в EUR = int"
#                 "конвертированная сумма в CHF = int"
#                 "конвертированная сумма в GBP = int"
#                 "конвертированная сумма в CNY = int"
#
#     3. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     4. Валюту пользователя определите сами.

def exchanger(currency, currency_rate):
    return currency * currency_rate


def negativeNumber(num):
    return num <= 0


def notIntNumber(num):
    return num * 100 % 100 != 0


currency_rates = {'usd': 0.013, 'eur': 0.011, 'uah': 0.36, 'chf': 0.012, 'byn': 0.03}
amount = input().strip()
if amount == "":
    print('Вы ввели пустое поле. Введите число.')
else:
    try:
        if negativeNumber(float(amount)):
            print('Введите положительное число.')
        elif notIntNumber(float(amount)):
            print('Вы ввели не целое число.')
        else:
            print('Ты ввёл', amount, 'RUB')
            for i, j in currency_rates.items():
                print('конвертированная сумма в', i.upper(), '=', round(exchanger(int(amount), j), 2), i.upper())
    except ValueError:
        print('Вы ввели не число. Введите число.')