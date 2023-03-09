#Задание 3.2
#Найти минимальный элемент.
#Вывести индекс минимального элемента на экран.
a=[int(x) for x in input().split()]
m=min(a)
for i in range(len(a)):
    if a[i]==m: print(m,' ',end='')
print()