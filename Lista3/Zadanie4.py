import qrcode
import os
import cv2

def QrCodeMaker(Dane,SciezkaZapisania,Nazwa="QrCode"):
    """
    Funkcja tworzy obrazek codu qr zawierajacy informacje podane przez uzytkownika
    Input:
    Dane(any) - Dane do stworzenia kodu qr
    ScizekaZapisania(str) - Sciezka do miejscsca gdzie obrazek ma zostac zapisany
    Nazwa(str) - Nazwa zapisania pliku kodu qr
    """
    print(Dane)
    qr = qrcode.QRCode()
    qr.add_data(Dane)
    qr = qr.make_image(fill_color = "black",back_color = "red")
    qr.save(os.path.join(SciezkaZapisania + "\\" + Nazwa + ".png"))

def QRCodeDecoder(SciezkaZapisania):
    '''
    Funkcja okdodowuje dany obrazek kodu qr
    Input:
    SciezkaZapisania(str) - Sciezka do miejsca gdzie znajduje sie kod qr do odczytania
    Output:
    Dane okdodowane z kodu qr
    '''
    qrim = cv2.imread(SciezkaZapisania)
    qr = cv2.QRCodeDetector()
    Dane = qr.detectAndDecodeMulti(qrim)
    print(Dane[1][0])


QrCodeMaker("abbbbcasd","D:\Programowanie\Semestr2\Lista3")
QRCodeDecoder("D:\Programowanie\Semestr2\Lista3\QrCode.png")