#Задание 1.1
#Считать с клавиатуры три произвольных числа,
#найти минимальное среди них и вывести на экран
a = int(input('введите первое число: '))
b = int(input('введите второе число: '))
c = int(input('введите третье число: '))
print('минимальное является: ', end='')
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
elif a >= c <=b:
    print(c)





