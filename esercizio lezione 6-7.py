class CSVFile :
    def __init__(self,name):
self.name = name
def get_data() :
    file = open(self.name)
    data = []
    for line in file :
        data.append(line split,strip())



        #esercizio 2
         
 class CSVFile : 
    def __init__(self,name):
        self.name = name
        def get_data() :
            data = []
            try:
                file = open (line split,strip())
                return data
            except :
                print ("erreur : file non trovato")
                return none

                #esercizio 3

                class numericalCSVFile(CSVFile):
                    def get_data(self) :
                        data = super().get-data()
                        new_data = []
                        for line in data :
                            try :
                        data = line ([0])
                        number = float ([0])
                        new_dataappend ([data,number])
                    except :
                    print(error:"row")
                    return newdata


#esercizio 4
from datetime import datetime
oggi = datetime.now()
anno = int (input("inserire il tuo anno di nascita :"))
mese = int(input("inserire il tuo mese di nascita :"))
giorno = int (input("giorno":))
anno_attuale = 2026 
mese_attuale = 3
eta =mese_attuale - anno  
if mese > mese_attuale :
    eta = eta - 1 
    print ("La tue età è :" , età)
if mese >= mese_attuale : 
    resto = mese -mese_attuale
else:
    resto = 12 -(mese_attuale - mese)
    print ("mesi prima del compleano :" , resto)


    #esercizio 5

    whiletrue  :
    print ("1.addizione") 
    print("2.differenza")
    print("3.uscire")
    scelta = input ("scelta(1,2,3):")
    if scelta == "1"
    a = int (input("numero1:"))
    b = int (input("numero2:"))
    print("risultato:",a+b)
elif choix == "2":
a = int(input("numero 1 :")) 
b = int (input("numero 2 : "))
print ( "resultato :" a-b)
elif scelto == "3"
print ("aao")
break
else :
print("error : scelto 1,2,3") 


















