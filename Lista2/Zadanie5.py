from PIL import Image 
import os
from pathlib import Path

def ZnakWodny(SciezkaObrazka,SciezkaZnakuWodnego,SciezkaZapisania):
    im = Image.open(SciezkaObrazka)
    ZnakWodny = Image.open(SciezkaZnakuWodnego)
    ZnakWodny = ZnakWodny.convert("RGBA")
    ZnakWodny.putalpha(128)
    ZnakWodny.show()
    w1,h1,w2,h2 = im.width//2 , im.height//2, ZnakWodny.width//2, ZnakWodny.width//2
    im.paste(ZnakWodny,(w1-w2,h1-h2), mask=ZnakWodny)
    im.save(os.path.join(SciezkaZapisania,Path(SciezkaObrazka).stem) + "_watermark.jpg")

ZnakWodny(SciezkaObrazka="D:\Programowanie\Semestr2\Lista2\Obrazek.jpg",SciezkaZnakuWodnego="D:\Programowanie\Semestr2\Lista2\ZnakWodny.jpg",
SciezkaZapisania="D:\Programowanie\Semestr2\Lista2")
        


