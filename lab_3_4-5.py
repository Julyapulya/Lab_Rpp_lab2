#Вывести в одну строку все положительные числа массива.
#Вывести в одну строку все отрицательные числа массива.
a,b,c=[int(x) for x in input().split()],[],[]
for x in a:
    if x>0: b.append(x)
    else: c.append(x)
print(*b); print(*c)