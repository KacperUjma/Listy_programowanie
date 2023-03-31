import string
import re

a = "9999*59"
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
        elif znak =='*':
            Lista.append(Liczby[i:index])
            i = index +1
        elif index == len(Liczby)-1:
            Lista.append(Liczby[i:])
    if not ("*" in Znaki or "*-" in Znaki) : 
        for i in Lista:
            suma += int(i)
        for i in range(len(Lista)):
            print (str(Lista[i]).center(30-len(str(Lista[i]))))
        print("+--------\n".center(30-9),str(suma).center(19-len(str(suma))))
    else: 
        for i in range(len(Lista)):
            print (str(Lista[i]).center(30-len(str(Lista[i]))))
        print("*---------".center(30-9))
        Dodwanie = 0
        Suma = 0
        for i in range(len(str(Lista[-1]))):
            Dodwanie = (int(Lista[0])*int(str(Lista[-1])[-(i+1)]))
            a = 30-i-len(str(Dodwanie))
            print(str(Dodwanie).center(a-i))
            Suma += Dodwanie*(10**i)
        print("+---------".center(30-9))
        print(str(Suma).center(30-len(str(Suma))))


DodawaniePodKreske(a)

