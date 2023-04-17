import os
from zipfile import ZipFile
from datetime import date
from datetime import date , timedelta , datetime


def Kopia(SciezkiFolderow = None, SciezkaZapisania = 'C:\\Backup', Rozszerzenie = None):
    """
    Funkcja tworzy skompresowaną kopię plików o podanym rozszerzeniu modyfikowanyh w ostatnich 3 dniach w formacie ZIP.
    Input:
    SciezkiFolderow(list) - Lista ścieżek do folderów (str), które mają być przeszukane.
    SciezkaZapisania(str) - Ścieżka miejsca, gdzie mają być zapisane skompresowane pliki.
    Rozszerzenie(str) - Rozszerzenie pliku, który ma być skopiowany.
    """
    with ZipFile(os.path.join(SciezkaZapisania,"copy-{data}".format(data=date.today())), 'w') as Kopia:
        for Folder in SciezkiFolderow:
            basename = os.path.basename(Folder)
            for NazwaFolderu, PodFoldery, NazwyPlikow in os.walk(Folder):
                for NazwaPliku in NazwyPlikow:
                    DataModyfikacji = os.path.getatime(os.path.join(NazwaFolderu,NazwaPliku))
                    DataModyfikacji = datetime.fromtimestamp(DataModyfikacji)
                    print(DataModyfikacji,NazwaPliku)
                    if DataModyfikacji >= datetime.today() - timedelta(days=3):        
                        if NazwaPliku.endswith(Rozszerzenie):
                            SciezkaPliku = os.path.join(basename, os.path.relpath(os.path.join(NazwaFolderu, NazwaPliku), start=Folder))
                            Kopia.write(os.path.join(NazwaFolderu, NazwaPliku), arcname=SciezkaPliku)


Kopia(['D:\Programowanie\Semestr2\Lista2\Folder do zip','D:\Programowanie\Semestr2\Lista2\Folder do zip2'],
'D:\Programowanie\Semestr2\Lista3',Rozszerzenie='.txt')