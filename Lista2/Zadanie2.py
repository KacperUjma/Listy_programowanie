from PIL import Image
import sys

def Miniaturka(Rozmiar = (128,128),SciezkaOtwarcia='D:\Programowanie\Semestr2\Lista2\Obrazek.jpg',
    SciezkaMiniatury='D:\Programowanie\Semestr2\Lista2',NazwaMiniatry=None):
    """
    Funkcja Tworzy z podanego obrazka jego miniaturke i zapisuje ja we wskazanym przez uzytkownika miejscu w formacie .jpg
    Input:
    !!! Romziar(tuple) - Wymiary miniatury
    SciezkaOtwarcia(str) - Cala sciezka pliku obrazka
    SciezkaMiniatury(str) - Sciezka do miejsca zapisania pliku miniatury
    NazwaMiniatury(str) - Nazwa pliku miniatury
    """
    try:
        im = Image.open(SciezkaOtwarcia)
    except: raise WindowsError('podales zla sciezke do pliku')

    if im.size[0]<Rozmiar[0] or im.size[1]<Rozmiar[1]:
        sys.exit("Probujesz zmiejszyc obrazek do rozmiarow wiekszych niz sam obrazek")

    if NazwaMiniatry == None:
        temp = SciezkaOtwarcia.split('\\')[-1]
        NazwaMiniatry = temp.split('.')[0] + '_Miniatura.jpg'
    else: NazwaMiniatry += '.jpg'

    im.thumbnail(Rozmiar)
    SciezkaMiniatury += "\\"+NazwaMiniatry
    im.save(SciezkaMiniatury)

Miniaturka()

