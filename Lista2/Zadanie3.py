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
    for Folder in SciezkiFolderow:
        with ZipFile(SciezkaZapisania + '\\' + str(date.today()) + '-' + os.path.basename(Folder) + '.zip','w') as Kopia:
            for NazwaFolderu, PodFoldery, NazwyPlikow in os.walk(Folder):
                for NazwaPliku in NazwyPlikow:
                    SciezkaPliku = os.path.join(NazwaFolderu,NazwaPliku)
                    Kopia.write(SciezkaPliku, os.path.basename(SciezkaPliku))

Kopia(['D:\Programowanie\Semestr2\Lista2\Folder do zip','D:\Programowanie\Semestr2\Lista2\Folder do zip2'],'D:\Programowanie\Semestr2\Lista2')
