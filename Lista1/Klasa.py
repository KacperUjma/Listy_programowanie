import numpy as np
import random
import math

class Vector(object):
    def __init__ (self,e=3):
        """
        Funkcja __init__ tworzy liste elementów wektora składającą się z 3 0        
        """
        self.Elementy = []
        for i in range(e):
            self.Elementy.append(0)

    def LosowaGeneracja(self):
        """
        Funkcja LosowaGeneracja zastępuje elementy vectora losowo wybranymi na przedziale (-10,10)
        """
        for i in range(len(self.Elementy)):
            a = random.uniform(-10,10)
            a = round(a,2)
            self.Elementy[i] = a

    def Wczytywanie(self,Lista):
        """
        Funkcja zmienia elementy wektora na podane przez uzytkownika
        Input:
        Lista(list) - Lista nowych elemetów wektora
        """
        if len(self.Elementy)==len(Lista):
            self.Elementy = Lista
        else: raise ValueError("Wektory roznej dlugosci")

    def __add__ (self,V):
        """
        Funcka dodaje elementy wektorów pierwszy z pierwszy drugi z drugim itd.
        Input:
        V(Vector/list) - Lista elementow ktore dodajemu do wektora
        Output:
        self.Elementy(list) - Lista nowych elementow wektora po dodaniu
        """
        j=0
        if len(self.Elementy)==len(V):
            for i in self.Elementy:
                a = round(i+V[j],2)
                self.Elementy[j] = a
                j+=1
            return self.Elementy
        else: raise ValueError("Wektory roznej dlugosci")

    def __sub__ (self,V):
        """
        Funcka odejmuje elementy wektorów pierwszy z pierwszy drugi z drugim itd.
        Input:
        V(Vector/list) - Lista elementow ktore odejmujemy od wektora
        Output:
        self.Elementy(list) - Lista nowych elementow wektora po odjeciu
        """
        j=0
        if len(self.Elementy)==len(V):    
            for i in self.Elementy:
                a = round(i-V[j],2)
                self.Elementy[j] = a
                j+=1
            return self.Elementy
        else: raise ValueError("Wektory roznej dlugosci")

    def __mul__ (self,A):
        """
        Funkcja przemnaza wektor przez skalar
        Input:
        A(float) - stala przz ktora bedziemy mnozyc wektor
        Output:
        self.Elementy(list) - lista elementow wektora przemnozonych przez skalar
        """
        for i in range(len(self.Elementy)):
            a = self.Elementy[i]*A
            self.Elementy[i]=a
        return self.Elementy

    def Dlugosc (self):
        """
        Funckja oblicza dlugosc wektora
        Output:
        round(math.sqrt(a),2)(float) - wartosc dlugosci wektora zaokraglona do dwoch miejsc po przecinku
        """
        a=0
        for i in self.Elementy:
            a += i**2
        return round(math.sqrt(a),2)

    def Suma(self):
        """
        Funkcja dodaje do siebie wszystkie elementy wektora
        Output:
        a(float) - suma elementow wektora
        """
        a=0
        for i in self.Elementy:
            a += i
        return a

    def IloczynSkalarny(self,V):
        """
        Funckaj wylicza iloczyn skalarny dwoch wektorow w postaci llisty
        Input:
        V(Vector/list) - wektor/lista przez ktora bedziemy mnozyc wektor 
        Output:
        S(float) - wynik pomnozenia skalarnego dwoch wektorow
        """
        S = 0
        if len(self.Elementy)==len(V):
            for i in range(len(self.Elementy)):
                S += self.Elementy[i]*V[i]
            return S
        else: raise ValueError("Wektory roznej dlugosci")
        
    def __str__(self):
        """
        Funkcja daje uzytkownikowi mozliwosc slownej interpretacji klasy wektor
        Output:
        self.Elementy(list) - lista elementow wektora
        """
        return "{self.Elementy}".format(self=self)

    def __getitem__ (self,i):
        """
        Funkcja umozliwia uzytkownikowi dostep do konkretnych elementow wektora poprzez odwolanie sie []
        Ipnut:
        i(intiger) - miejsce elementu do ktorego uzytkownik chce sie odwolac
        Output:
        self.Elementy[i](float) - element z miejscac i
        """
        return self.Elementy[i]
    
    def __contains__(self,a):
        """
        Funkcja umozliwia uzytkownikowi sprawdzenie czy wpisany element jest jednym z elementow wektora
        Input:
        a(float) - element do sprawdzenia czy jest elementem wektora
        Output:
        a in self.Elementy(bool) - wyrazenie logiczne sprawdzajace czy a jest elementem wektora
        """
        return a in self.Elementy
    
    def __len__(self):
        """
        Funkcja daje uzytkownikowi mozliwosc sprawdzenia z ilu elementow sklada sie wektor
        Output:
        len(self.Elementy)(int) - zwraca ilosc elementow wektora
        """
        return len(self.Elementy)


