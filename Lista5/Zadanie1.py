from tkinter import *
from tkinter import ttk
import tkinter as tk
import requests
import os
from datetime import datetime

def Pzrelicznik():
    '''
    Funkcja przelicza waluty podane w combobox'ach
    Output:
    Wynik(float) - zwraca przeliczona walute z dokladnoscia do 4 miejsc po przeciunku
    '''
    od = WalutaWejsciowa.get()
    do = WalutaWyjsciowa.get()
    Pieniadze = float(Kwota.get())
    kurs = round(Slownik[f'{od}']/Slownik[f'{do}'],4)
    Pieniadze *= kurs
    Wynik.set(float(Pieniadze))
    return Wynik

def Zakoncz():
    '''Funkcja konczy dzialanie programu'''
    root.destroy()

def PobieranieDanych(url):
    '''
    Funckja próbuje pobrac dane z internetu, w przypadku 
    gdy moze tworzy listy z nazwami walut, przlicznikami oraz slownik bedacy ich zlozeniem, uaktualnia takze zapisane w pliku dane dotyczace walut
    gdy nie moze pobiera dane z plikow tekstowych, jesli nie ma takiej mozliwosci zwraca blad
    Output:
    ListaNazw(list) - Lista nazw walut
    ListaWalut(list) - Lista kursow walut
    Slownik(dict) - Slownik gdzie nazwy walut sa kluczami, a kursy argumentami 
    '''
    global CzasPobraniaDanych
    try:
        dane = requests.get(url)
        dane  = dane.json()[0]['rates']
        ListaNazw = ['zloty (Polska) PLN']
        ListaWalut = [1]
        CzasPobraniaDanych = datetime.today().replace(microsecond=0)
        for i in range(len(dane)):
            ListaNazw.append(dane[i]['currency']+" "+dane[i]['code'])
            ListaWalut.append(dane[i]['mid'])
        Slownik = dict(zip(ListaNazw,ListaWalut))
        with open('NazwyWalut.txt','w') as f:
            for x in ListaNazw:
             f.write(f'{x}\n') 
            f.write(str(CzasPobraniaDanych))  
        with open('KursyWalut.txt','w') as f:
            for x in ListaWalut:
                f.write(f'{x}\n')
        return ListaNazw, ListaWalut, Slownik
    except:
        if os.path.exists('NazwyWalut.txt') and   os.path.exists('KursyWalut.txt'):
            with open('Nazwywalut.txt','r') as f:
                lines = f.readlines()
                ListaNazw = [line.strip() for line in lines]
                CzasPobraniaDanych = ListaNazw.pop()
            with open('KursyWalut.txt','r') as f:
                lines = f.readlines()
                ListaWalut = [float(line.strip()) for line in lines]
            Slownik = dict(zip(ListaNazw,ListaWalut))
            return ListaNazw, ListaWalut, Slownik
        else: 
            OSError("Brak mozliwosci pobrania dancyh")

ListaNazw = PobieranieDanych(url := 'http://api.nbp.pl/api/exchangerates/tables/A')[0]
ListaWalut = PobieranieDanych(url)[1]
Slownik = PobieranieDanych(url)[2]

root = Tk()
root.title("Kalkulator walut")
# zmienne
Kwota = tk.StringVar()
WalutaWejsciowa = tk.StringVar(value = ListaNazw[0])
WalutaWyjsciowa = tk.StringVar(value = ListaNazw[2])
Wynik = StringVar()
# obsluga okienka
mainframe = ttk.Frame(root,padding=10)
mainframe.grid()
ttk.Label(mainframe,text="Wybierz walute wejsciowa").grid(row=1,column=3)
ttk.Combobox(mainframe, textvariable=WalutaWejsciowa, values=ListaNazw,width=40,state='readonly').grid(row=2,column=3)
ttk.Label(mainframe,text="Wybierz walute wyjsciowa").grid(row=4,column=3)
ttk.Combobox(mainframe, textvariable=WalutaWyjsciowa, values=ListaNazw,width=40,state='readonly').grid(row=5,column=3)
ttk.Label(mainframe,text="Wpisz ile waluty chcesz przeliczyc").grid(row=1,column=1)
ttk.Entry(mainframe,textvariable=Kwota).grid(row=2,column=1)
ttk.Button(mainframe,text="Przelicz",command=Pzrelicznik).grid(row=2,column=5)
ttk.Label(mainframe,text="Wynik:").grid(row=4,column=1)
ttk.Label(mainframe,textvariable=Wynik,state="readonly").grid(row=5,column=1)
ttk.Button(mainframe,text="Zakoncz",command=Zakoncz).grid(column=5)
ttk.Label(mainframe,text="Dane z \n" + str(CzasPobraniaDanych),font=(None,6)).grid(column=1,row=7)

root.mainloop()