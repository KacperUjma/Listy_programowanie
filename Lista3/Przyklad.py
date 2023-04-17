from datetime import date , timedelta,datetime
import os

def Sprawdzanie(Plik,Rorszerzenie):
    return Plik.endswith(Rorszerzenie)


a = os.path.getatime('D:\Programowanie\Semestr2\Lista2\Zadanie1.py')
b = datetime.fromtimestamp(a)
print(date.today(),a,b,b - timedelta(days=3))
if b < b -timedelta(days=3):
    print(True)
else: print(False)

