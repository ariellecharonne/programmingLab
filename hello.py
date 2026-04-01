# esercizio 1
ore = 538
minuti = 538-(8*60) #58min
print(f"{int(ore)}, {minuti}")
# esercizio 2(quadrato e cubo)
x=int(input("inserire un numero intero"))
quadrato=x*x
cubo=x*x*x
print("quadrato",quadrato)
print("cubo",cubo)
# esercizio 3(verificare se un numero e pari )
x=int(input("inserire un numero intero"))
if x%2 == 0:
 print("numeri pari")
else:
 print("numero dispari") 

# esercizio 4(comtare quanto di volta una lettra ....)
def conta_lettura(parola,lettera):
    return parola.count(lettera)
print(conta_lettura("banana","a"))

# esercizio 5(verificare se un numero e primo)
x=int(input("inserisci un numero:"))
primo=True
if x < 2:
    primo=False
else:
   for i in range (2,x):
      if x % i ==0:
         primo=False
         break
      
      if primo:
         print("numero primo")
if primo:
   print("numero primo")
else:
   print("non e primo ")
   # 
   
   # esercizio 6(somma di n numero)  
somma = 0
while True:
   n= int(input("inserisci un numero(0 per fermare):"))
   if n ==0:
      break
   somma += n

   print("somma totale:", somma)

# esercicio 7(fontion factorielle)
def fattoriale(n):
   risultato = 1
   for i in range(1,n+1):
      risultato = risultato * i
      return risultato 
   
   print(fattoriale(5))

   #esercizio 8(verifier le type de triangle)
   def tipo_triangolo(a,b,c):
      if a + b > c and a + c > b and b + c > a:
         if a == b == c:
            return "Triangolo equilatero"
         elif a == b or a == c or b == c:
            return "triangolo isoscele"
         else:
            return "Triangolo scaleno"
      else:
         return "Non e un triangolo"

      print( tipo_triangolo(3,3,3))

      #esercizio 9(conter les voyelles)
      def conta_vocali(stringa):
         vocali = "aeiou"
         count = 0 
         for lettera in stringa:
            if lettera in vocali:
               count += 1 
               return count 
            
            print(conta_vocali("programmazione"))


 
 




