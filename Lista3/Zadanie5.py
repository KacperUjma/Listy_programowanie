import sys
WyrazenieMatematyczne1 = "[1+(3*2/1-32)+{2^3}*<1-2>]"
WyrazenieMatematyczne2 = "(1+[2-4*{2/<3-1>+1}])"
class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):              
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):            
        return False

    def push(self, item):
        self.items.append(item)

    def pop(self):                     
        return self.items.pop()   
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self,i):
        return self.items[i]
    
    def __contains__(self,i):
        return i in self.items
    
def Sprawdzanie(Lancuch):
    '''
    Fuunkcja sprawdza czy w podanym wyrazeniu matematycznym nawiasy sa dobrze osadzone
    Input:
    Lancuch(str)-wyrazenie matematyczne
    Output:
    Bool -  w zaleznosci od poprawnosci wyrazenia
    '''
    StosLewo = Stack()
    StosPrawo = Stack()
    NawiasyLewostronne = ['(','{','[','<']
    NawiasyPrawostronne = [')','}',']','>'] 
    Nawiasy = {'(':')' , '{':'}' , '[':']' , '<':'>'}

    for i in Lancuch:
        if i in NawiasyLewostronne:
            StosLewo.push(i)
        elif i in NawiasyPrawostronne:
            StosPrawo.push(i)

        for i in range(len(NawiasyLewostronne)-1):
            if NawiasyLewostronne[i] == NawiasyLewostronne[i+1] or NawiasyPrawostronne[i] == NawiasyPrawostronne[i+1]:
                sys.exit("Wyrazenia ma dwa takie same nawiasy kolo siebie")


    print(StosLewo,StosPrawo)
    if len(StosLewo) == len(StosPrawo):
        for i in StosLewo:
            if Nawiasy.get(i) == StosPrawo.pop():
                continue
            else: 
                print("Nawiasy nie zgadzdaja sie")
                return False
    else: sys.exit("Ilosc nawiasow lewo i praowostronnych nie zgadzaja sie")
    print("Wyrazenie jest zgodne pod wzgledem nawiasow")
    return True


Sprawdzanie("({<([{}])>})")
