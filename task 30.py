# Задача 30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

n = int(input('Введите количество элементов прогресси: '))
a = [0]*n
a[0] = int(input('Введите первый элемент прогрессии: '))
d = int(input('Введите разность прогрессии: '))
print(a[0],end=' ' )
for i in range(1,n):
    a[i]= a[i-1]+d
    print(a[i],end=' ')


#или

# a1 = int(input('Введите первый элемент прогрессии: '))
# d = int(input('Введите разность прогрессии: '))
# n = int(input('Введите количество элементов прогресси: '))
# arr = []
# for i in range(n):
#     c = a1 + i*d
#     arr.append(c)
# print(arr,end=' ' )