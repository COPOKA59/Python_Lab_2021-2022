a=int(input('Введите номер дня первого числа месяца '))
b=int(input('Введите число месяца '))
print('Номер дня недели ', b, '-го числа равен ', (a+b-1)%7, sep='')