#1

#number = int(input('Введите число: '))
#print(number, number+1, number+2, sep='\n');



'''
#2

x1 = int(input('Введите первое число: '))
x2 = int(input('Введите второе число: '))
x3 = int(input('Введите третье число: '))

print(x1+x2+x3)
'''


'''
#3

x = int(input('Введите длину ребра куба: '))

v = x **3
s = 6 * x **2

print('Объём куба: ', v)
print('Площадь поверхности куба: ', s)

'''


'''
#4

a = int(input('Введите значение переменной a: '))
b = int(input('Введите значение переменной b: '))

x = 3 * (a+b)**3 + 275 * b**2 - 127 * a - 41

print('x: ', x)

'''

'''
#5

x = int(input('Введите значение: '))

print('Следующее за числом', x, 'число:', x+1)
print('Для числа', x, 'предыдущее число:', x-1)

'''

'''
#6

display  = int(input('Введите стоимость монитора: '))
pc       = int(input('Введите стоимость системного блока: '))
keyboard = int(input('Введите стоимость клавиатуры: '))
mouse    = int(input('Введите стоимость мыши: '))

print('Цена трёх таких наборов:', 3 * (display + pc + keyboard + mouse))

'''

'''
#7

a_1 = int(input('Введите первое значение: '))
d   = int(input('Введите второе значение: '))
n   = int(input('Введите третье значение: '))

a_n = a_1 + d * (n - 1)

print('Арифметическая прогрессия:', a_n)

'''

# Разделяй и властвуй
'''
x = abs(int(input('Введите значение: ')))
print(x, x * 2, x * 3, x * 4, x * 5, sep='---')
'''

# Мандарины
'''
n = int(input('Количество человек: '))
k = int(input('Количество мандаринов: '))

x = k // n

print('Количество мандаринов для каждого человека:', x)
print('Количество мандаринов в корзине:', k - (x * n))
'''

#Сама неотвратимость
'''
nn = int(input('Введите население: '))

print(nn//2 + nn%2)
'''

#Пересчет временного интервала
'''
min = int(input('Введите количество минут: '))
hours = min // 60
min_last = min - (hours * 60)

print(min, 'мин - это', hours, 'час', min_last, 'минут.')
'''

#Трехзначное число
'''
x = int(input('Введите первое значение: '))

x1 = x % 10
x2 = (x % 100) // 10
x3 = x // 100

print()
print('Сумма чисел:', x1 + x2 + x3)
print('Произведение чисел:', x1 * x2 * x3)
'''

#Пингвины
'''
n = int(input('Введите количество пингвинов: '))

print('    _~_    ' * n)
print('   (o o)   ' * n)
print('  /  V  \  ' * n)
print(' /(  _  )\ ' * n)
print('  ^^   ^^  ' * n)
'''

# Вторая справа цифра
'''
x = int(input('Введите значение:'))

print(x // 10 % 10)
'''

# Электронные часы
'''
min = abs(int(input('Введите число: ')))

hours = min % (60 * 24) // 60
min_last = min % 60

print(hours,":",min_last)
'''

# 0 в 1 и наоборот
'''
x = int(input('Введите число: '))
print(1 - x)
'''

#Следующее четное
'''
x = int(input('Введите значение: '))
print((x // 2 + 1) * 2)
'''

#МКАД
'''
speed = int(input('Введите скорость: '))
time  = int(input('Введите время: '))

x = speed * time
n = x // 109
print(-(109 * n - x))
'''

#Улитка*

h = int(input('Введите высоту: '))
a = int(input('Введите A: '))
b = int(input('Введите B: '))
print((h - a) // (a - b) + 1)
