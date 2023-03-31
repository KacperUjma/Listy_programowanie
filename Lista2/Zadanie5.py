from PIL import Image 
import os
from pathlib import Path

def ZnakWodny(SciezkaObrazka,SciezkaZnakuWodnego,SciezkaZapisania):
    '''
    Funckja dodaje znak wodny do obrazka poprzez nalozenie na niego podanego znaku wodnego zwiekszajac jego przezroczystosc
    Input:
    SciezkaObrazka(str) - Sciezka zapisania pliki obrazka na ktory zostanie nalozony znak wodny
    SceizkaZnakuWodnego(str) - Sciezka zzapisania pliku obrazka ktory zostanie uzyty do znaku wodnego
    SciezkaZapisania(str) - Sciezka gdzie ma zostac zapisany nowy obrazek z naniesionym znakiem wodnym bez nazwy zapisania
    '''
    im = Image.open(SciezkaObrazka)
    ZnakWodny = Image.open(SciezkaZnakuWodnego)
    ZnakWodny = ZnakWodny.convert("RGBA")
    ZnakWodny.putalpha(128)
    w1,h1,w2,h2 = im.width//2 , im.height//2, ZnakWodny.width//2, ZnakWodny.width//2
    im.paste(ZnakWodny,(w1-w2,h1-h2), mask=ZnakWodny)
    im.save(os.path.join(SciezkaZapisania,Path(SciezkaObrazka).stem) + "_watermark.jpg")

ZnakWodny(SciezkaObrazka="D:\Programowanie\Semestr2\Lista2\Obrazek.jpg",SciezkaZnakuWodnego="D:\Programowanie\Semestr2\Lista2\ZnakWodny.jpg",
SciezkaZapisania="D:\Programowanie\Semestr2\Lista2")
        


