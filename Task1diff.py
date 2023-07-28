'''задача 1 необязательная. Напишите программу, которая получает целое число и возвращает его двоичное,
восьмеричное строковое представление.
Функции bin и oct используйте для проверки своего результата.
*Дополнительно Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
Избегайте магических чисел Добавьте аннотацию типов где это возможно
Используйте функции'''
import os, random
os.system('cls')
def DecimalToBin (x:int)->str:
    s:str = str()
    if x==0:
        return str(0) 
    while x>=1:
        s=str(x%2)+s
        x//=2
    return s
def DecimalToOctal (x:int)->int:
    octal:list =[]
    if x in range(7):
        return str(x)
    while x/8>=1:
        octal.insert(0,x%8)
        x=x//8
    octal.insert(0,x)
    return str(octal).replace(', ','').replace('[','').replace(']','')
set:set= set()
for i in range(1000):
    set.add(DecimalToBin(i)==str(bin(i)[2:]))
if False in set:
    set.remove(True)
print(set)
set.clear
for i in range(1000):
    set.add(DecimalToOctal(i)==str(oct(i)[2:]))
    if DecimalToOctal(i)!=str(oct(i)[2:]):
        print(i)
if False in set:
    set.remove(True)
print(set)
