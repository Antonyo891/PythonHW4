'''Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод
— на i-ом кусте выросло a[i] ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один 
заход собирающий модуль, находясь перед некоторым кустом заданной во входном списке урожайности грядки.'''
import os, random
os.system('cls')
def MaxNumberOfBerry (list1:list)->int:
    maxNumberOfBerry:int=list1[-1]+list1[0]+list1[1]
    for i in range(1,len(list1)):
        if i==len(list1)-1:
            if maxNumberOfBerry<list1[i-1]+list1[i]+list1[0]:
                maxNumberOfBerry=list1[i-1]+list1[i]+list1[i+1]   
        elif maxNumberOfBerry<list1[i-1]+list1[i]+list1[i+1]:
            maxNumberOfBerry=list1[i-1]+list1[i]+list1[i+1]
    return maxNumberOfBerry
mapOfBush:list = list()
numberOfBush = int(input ('Сколько кустов черники на ферме '))
for i in range(numberOfBush):
#    mapOfBush.append(random.randint(1,10))
    mapOfBush.append(int(input(f'Введите урожайность {i+1} куста ')))
print(mapOfBush)
maxNumberOfBerry:int = MaxNumberOfBerry(mapOfBush) #answer
print(maxNumberOfBerry)
