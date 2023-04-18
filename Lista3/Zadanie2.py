import os

def ZamianaZnakuKoncaLinii(SciezkaPliku,SciezkaZapisania ,Nowyznak):
    Nowyznak = Nowyznak.lower()
    if Nowyznak == 'widnows':
        Nowyznak = '\r\n'
    elif Nowyznak == 'unix':
        Nowyznak = '\n'

    with open(SciezkaPliku,'r',newline='') as Odczyt:
        Zawartosc = Odczyt.read()

    Zawartosc = Zawartosc.replace('\r\n','\n').replace('\n',Nowyznak)

    with open(os.path.join(SciezkaZapisania,'Plik_ze_Zmiana_Znaku.txt'),'w',newline=None) as Plik:
        Plik.write(Zawartosc)

ZamianaZnakuKoncaLinii('D:\Programowanie\Semestr2\Lista3\\file-sample_100kB.txt','D:\Programowanie\Semestr2\\Lista3','Unix')
