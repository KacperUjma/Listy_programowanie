import string
import re

a = "12-4"
print(len(a))
def DodawaniePodKreske(Liczby):
    '''
    Funkcja tworzy zapis dodawania lub odejmowania pod kreske danego zadania
    Liczby(str) - ciag liczb dodawanych lub odejmowanych od siebie
    '''
    Znaki = re.findall(r"[\W]+",Liczby)
    Lista =[]
    i = 0
    suma = 0
    for index,znak in enumerate(Liczby):
        if znak == '+':
            Lista.append(Liczby[i:index])
            i = index + 1
        elif znak =='-':
            Lista.append(Liczby[i:index])
            i = index
        elif index == len(Liczby)-1:
            Lista.append(Liczby[i:])
    print(Lista)
    if not ("*" in Znaki or "*-" in Znaki) : 
        for i in Lista:
            suma += int(i)
        for i in range(len(Lista)):
            print (str(Lista[i]).center(30-len(str(Lista[i]))))
        print("+--------\n".center(30-9),str(suma).center(19-len(str(suma))))
    else: 
        for i in range(len(Lista)):
            print (str(Lista[i]).center(30-len(str(Lista[i]))))
        print("*---------\n".center(30-9))

DodawaniePodKreske(a)

