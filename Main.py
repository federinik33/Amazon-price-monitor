import Check
import time
import datetime

# Funzione check_price: check_price(float budget, str link)
link = []
budget = []
N_elementi = int(input("Inserisci il numero di articoli che vuoi controllare : "))
j = 0
while (j<N_elementi):
  link.append(input("Inserisci il link dell'articolo numero " + str(j + 1) + " : "))
  budget.append(float(input("Inserisci il prezzo sotto cui vuoi ricevere un avviso : ")))
  j += 1
print("\n")
while (True):
  j = 0
  x = datetime.datetime.now()
  print(x.strftime("%d/%m/%y %X"))
  while (j<N_elementi):
    Check.check_price(budget[j], link[j])
    j += 1
  print("\n---------------------------------------------------------\n")
  # loop that allows the program to regularly check for prices
  time.sleep(60*5)
