import Check
import time
import datetime

# Funzione check_price: check_price(float budget, str link)
link = []
budget = []
linea=[]
cont=0
f = open("amazon.txt", "r")
for x in f:
  linea.append(x)
  cont+=1
N_elementi = cont
j = 0
while (j<N_elementi):
  #Find ',' and split linea in budget and link
  prodotto=linea[j].split(',')
  link.append(prodotto[1])
  budget.append(float(prodotto[0]))
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
