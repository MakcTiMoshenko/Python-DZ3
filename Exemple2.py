"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине 
элемент к заданному числу X. Пользователь в первой строке вводит 
натуральное число N – количество элементов в массиве. В последующих  
строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5"""
    
import random
n = int(input("Введите количество чисел в списке: "))
x = int(input("Введите искомое число от 1 до 10, от которого будет найдено ближнее: "))
list = []

for i in range(n):
    list.append(random.randint(1, 10))
print(list)


for i in range (len(list)):
    if x+1 == list[i] or x-1 == list[i]:
        print(list[i])
        break
else: 
    print("Такого элемента нет")