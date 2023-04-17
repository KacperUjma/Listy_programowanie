import webbrowser
from bs4 import BeautifulSoup
import requests

def PropozycjaStron():
    '''
    Fukncja propounje uzytkownikowi 5 roznych artykuluw z Wikipedii, uzytkownik wpisujac tak lub nie ma mozliwosc otworzenia artykulu lub wyszukania nowego
    '''
    dic = {}
    dictitle = {}
    i=1
    Odpowiedz = 'nie'
    while Odpowiedz=='nie':
        Strona = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        soup = BeautifulSoup(Strona.content,features="html5lib")
        Tytul = soup.select_one('title').text
        print("Strona {index} to".format(index=(i)),Tytul)
        dic.update({i:Strona.url})
        dictitle.update({i:Tytul})
        Odpowiedz = str(input("Wpisz tak lub nie jesli zadowolil cie artykul o podanym tytule\n"))
        i += 1
        if Odpowiedz == 'tak':
            webbrowser.open_new(Strona.url)
            break
        if i==6:
            print("Proponowane strony to")
            for i in dic:
                print("Strona {index} to {Strona}".format(index=i,Strona=dictitle[i]))
            Odpowiedz = int(input("Wpisz numer strony ktora najbardziej cie zaciekawila a ja przekieruje cie na nia\n"))
            webbrowser.open_new(dic[Odpowiedz])
            break

PropozycjaStron()
