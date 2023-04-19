import os

def ZamianaZnakuKoncaLinii(SciezkaPliku,Nowyznak):
    '''
    Funkcja zmienia znak konca lini z unix na CR LF i odwrotnie
    '''
    Nowyznak = Nowyznak.lower()
    if Nowyznak == 'windows':
        Nowyznak = '\r\n'
    elif Nowyznak == 'unix':
        Nowyznak = '\n'

    with open(SciezkaPliku,'r',newline='') as Odczyt:
        Zawartosc = Odczyt.read()

    print(Zawartosc)

    if '\r\n' in Zawartosc:
        NowaZawartosc = Zawartosc.replace('\r\n','\n')
    elif '\n' in Zawartosc:
        NowaZawartosc = Zawartosc.replace('\n','\r\n')
    
    with open(SciezkaPliku,'w',newline='') as Plik:
        Plik.write(NowaZawartosc)

    print(NowaZawartosc)
    

ZamianaZnakuKoncaLinii('D:\Programowanie\Semestr2\Lista3\\file-sample_100kB.txt','windows')
