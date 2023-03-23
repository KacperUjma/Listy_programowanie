from PyPDF2 import PdfWriter
from pathlib import Path
import os

Rodzialy = [[0,10],[10,25],[30,40]]

def RodzielaniePDF(SciezkaPliku,SciezkaZapisania,Podzial):
    '''
    Funkcja rodziela zadany przez uzytkownika plik pdf na mniejsze podane o podanym przez uzytkownika podziale
    Input:
    SciezkaPliku(str) - Sciezka w ktorej zostal zapisany plik do podzialu
    SciezkaZapisania(str) - Sciezka zapisania pliku bez nazwy pliku
    Podzial(list) - Lista skaldajaca sie z dwuelementowych list bedocych podzialami stron na nowe pliki pdf
    '''
    for przedial in Podzial:
        with PdfWriter( os.path.join(SciezkaZapisania,Path(SciezkaPliku).stem) + '_' + str(przedial[0]+1) + '-' + str(przedial[1]+1) + '.pdf') as pdf:
            pdf.append(SciezkaPliku,(przedial[0],przedial[1]))

RodzielaniePDF("D:\Programowanie\Semestr2\Lista2\Fichtenholz_RachunekRozniczkowy.pdf","D:\Programowanie\Semestr2\Lista2",
Rodzialy)




