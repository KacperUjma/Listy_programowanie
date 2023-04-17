from PyPDF2 import PdfWriter
from pathlib import Path
import os

Pliki = ["D:\Programowanie\Semestr2\Lista3\pan-tadeusz_1-10.pdf","D:\Programowanie\Semestr2\Lista3\pan-tadeusz_31-40.pdf","D:\Programowanie\Semestr2\Lista3\pan-tadeusz_11-25.pdf"]

def LaczeniePDF(SciezkiPlikow,SciezkaZapisania,Nazwa="ZlaczonyPDF"):
    '''
    Funkcja tworzy jeden plik pdf z podanych przez uzytkownika
    Input:
    SciezkiPlikow(list) - Sciezki do plikow pdf ktore maja byc zlaczone
    SciezkaZapisania(str) - Sciezka zapisania pliku bez nazwy pliku
    Nazwa(str) - Nazwa utworzonego pliku pdf
    '''
    with PdfWriter(os.path.join(SciezkaZapisania + "\\" + Nazwa + ".pdf")) as pdf:
        for Plik in SciezkiPlikow:
            pdf.append(Plik)
            pdf.close()

LaczeniePDF(Pliki,"D:\Programowanie\Semestr2\Lista3")
