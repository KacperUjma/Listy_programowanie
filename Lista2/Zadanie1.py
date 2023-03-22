import string 
import random

s = string.ascii_letters + string.digits + string.punctuation
def GeneratorHasla(d=8,Lista = string.ascii_letters + string.digits + string.punctuation):
    """
    Funkcja generuje losowo wygenerowane haslo z listy znakow o dlugosi 8 
    Input:
    Lista(str/list) - Lista znakow uzytych do wygenerowania hasla
    d(int) - Dlugosc hasla
    Output:
    Haslo(str) - Losowo wygenerowane haslo 
    """
    Haslo = ""
    for i in range(d):
        r = random.randint(0,len(Lista)-1)
        Haslo += Lista[r]
    return Haslo

print("Haslo wygenerowane bez podanych argumentow",GeneratorHasla())
print("Haslo wygenerowane poprzez podana liste argumentow",GeneratorHasla(Lista=["a","b"]))
print("Haslo wygenerowane z 10 znakami",GeneratorHasla(d=10))
print("Haslo wygenerowane z 3 znakami poprzez podana liste argumentow",GeneratorHasla(d=3,Lista=["a","b"]))

    