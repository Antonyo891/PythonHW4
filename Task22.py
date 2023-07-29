'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. 
n — кол-во элементов первого множества. 
m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.'''
import os, random
os.system('cls')
#def ChoiseFromList (list1:list,list2:list)->set:
def FillingList (numberOfElement:int)->list:
    list1:list=[]
    for i in range(numberOfElement):
        list1.append(random.randint(0,15))
    return list1
list1:list=FillingList(55)
print(list1)
list2:list=FillingList(55)
print(list2)
set1:set=set(list1)
set2:set=set(list2)
set3:set=set.intersection(set1,set2)
if len(set3)==0:
    print('Нет чисел которые встречаются в обоих наборах')
else:
    print(set3)
