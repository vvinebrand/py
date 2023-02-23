# Задача 1: Найдите сумму цифр трехзначного числа.


def f_task():
    num = int(input('\nВведите трехзначное число: '))
    if 999 < num or num < 100:
        print('\nВы ввели не трехзначное число!')
    else:
        units = num % 10
        num = num // 10
        dozens = num % 10
        num = num // 10
        print(f'\nСумма цифр в числе равна: {num + units + dozens}')

stp = True
while stp:
    print('1. Найдите сумму цифр трехзначного числа\n2.')
    n = int(input('Введите номер задачи: '))
    if n == 1:
        f_task()
    else:
        print('Программа завершена')
        stp = False