import os
from zipfile import ZipFile
from datetime import date
def Kopia(SciezkiFolderow,SciezkaZapisania):
    '''
    Funkcja tworzy skomperoswana kopie plikow zadanych przez uzytkownika w formacie zip
    Input:
    SciezkiFolderow(list) - Lista scsiezek do folderow (str) ktore maja byc skompresowane
    SciezkaZapisania(str) - Sciezka miejsca gdzie maja byc zapisane skopresowane pliki
    '''
    
    with ZipFile(os.path.join(SciezkaZapisania,str(date.today())+"_Kopia.zip"),'w') as Kopia:
        for Folder in SciezkiFolderow:
            for NazwaFolderu, PodFoldery, NazwyPlikow in os.walk(Folder):
                Kopia.write(NazwaFolderu)
                for NazwaPliku in NazwyPlikow:
                    SciezkaPliku = os.path.join(NazwaFolderu,NazwaPliku)
                    Kopia.write(SciezkaPliku)

Kopia(['D:\Programowanie\Semestr2\Lista2\Folder do zip','D:\Programowanie\Semestr2\Lista2\Folder do zip2'],'D:\Programowanie\Semestr2\Lista2')
