'''задача 2 необязательная.
Даны два многочлена, которые вводит пользователь.
Задача - сформировать многочлен, содержащий сумму многочленов.
Степени многочленов могут быть разные.

например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
на выходе будет 5x^3 - x^2 + 4х - 7 = 0
можно использовать модуль re'''
import re,os,random
os.system('cls')
def PolynomialToDict (string:str)->dict:
    import re
    string1:str=''
    string=string.lower()
    for i in range(len(string)):
        if (string[i]=='+') or (string[i]==' ' and (string[i-1]==' ' or string[i-1]=='+' or string[i-1]=='-')):
            continue
        else:
            string1=string1+string[i]
    string1=string1.replace(' = 0','')
    list1:list=string1.split(' ')
    dict1:dict={}
    degreePolinimial:int=int((list1[0])[len(list1[0])-1])
    while degreePolinimial>=0:
        dict1[degreePolinimial]=0
        degreePolinimial-=1
    value:str=''
    for element in list1:
        if 'x^' in element:
            if '-' in element:
                if element[0]=='x':
                    dict1[int(element[len(element)-1])]=-1
                else:
                    value=re.match('\d+',element[1:]).end()
                    dict1[int(element[len(element)-1])]=int(element[:value+1])
            else:
                if element[0]=='x':
                    dict1[int(element[len(element)-1])]=1
                else:
                    value=re.match('\d+',element).end()    
                    dict1[int(element[len(element)-1])]=int(element[:value])
        elif 'x' in element and '^' not in element:
            if '-' in element:
                if element[0]=='x':
                    dict1[1]=-1
                else:
                    value=re.match('\d+',element[1:]).end()
                    dict1[1]=int(element[:value+1])
            else:
                if element[0]=='x':
                    dict1[1]=1
                else:
                    value=re.match('\d+',element).end()                    
                    dict1[1]=int(element[:value])
        else:
            if '-' in element:
                value=re.match('\d+',element[1:]).end()
                dict1[0]=int(element[:value+1])
            else:    
                value=re.match('\d+',element).end()
                dict1[0]=int(element[:value+1])       
    return dict1    
def SumPolynomialDict(dict1:dict, dict2:dict)->dict:
    list1:list=list(dict1.keys())
    list2:list=list(dict2.keys())
    degreePolinomia = 0
    dictSum:dict={}
    dictMin:dict={}
    if len(list1)>len(list2):
        dictSum=dict1
        degreePolinomia = len(list1)
        dictMin = dict2
    else:
        dictSum=dict2
        degreePolinomia = len(list2)
        dictMin = dict1
    while degreePolinomia>=0:
        if degreePolinomia in dictMin.keys(): 
            dictMin[degreePolinomia] = dictMin[degreePolinomia]
        else:
            dictMin[degreePolinomia] = 0
        degreePolinomia-=1
    for key,value in dictSum.items():
        dictSum[key]=value+dictMin[key]
    return dictSum
def StringPolynomFromDict(dict1:dict)->str:
    string:str=''
    degreepolynomia = len(list(dict1.keys()))
    for i in range(degreepolynomia):
        if dict1[i]==0:
            continue
        elif i==0:
            if dict1[i]>0:
                string=f" + {dict1[i]}"+ string
            elif dict1[i]<0:
                string=f" - {abs(dict1[i])}" + string 
        elif i==1:
            if dict1[i]==1:
                string = " + x"+string
            elif  dict1[i]==-1:
                string = f" - x"+string 
            elif dict1[i]<-1:
                string = f" - {abs(dict1[i])}x"+string
            else:
                string = f" + {dict1[i]}x"+string
        elif i==degreepolynomia-1:
            if dict1[i]==1:
                string = f"x^{i}"+string
            elif  dict1[i]==-1:
                string = f"- x^{i}"+string 
            elif dict1[i]<-1:
                string = f"- {abs(dict1[i])}x^{i}"+string
            else:
                string = f"{dict1[i]}x^{i}"+string
        elif i>1:
            if dict1[i]>1:
                string = f" + {dict1[i]}x^{i}"+string
            elif dict1[i]==1:
                string = f" + x^{i}"+string
            elif dict1[i]==-1:
                string = f" - x^{i}"+string
            else:
                string =f" - {abs(dict1[i])}x^{i}"+string
    string = string + " = 0"
    if string[:3]==' + ':
        string=string[3:]
    return string
string1:str= str('2x^2 + 4x + 5 = 0')
string2:str=str('5x^3 - 3*x^2 - 12 = 0')
print(string1)
print(string2)
dict1:dict=PolynomialToDict(string1)
dict2:dict=PolynomialToDict(string2)
SumPolynomial:dict=SumPolynomialDict(dict1,dict2)
print(StringPolynomFromDict(SumPolynomial))
