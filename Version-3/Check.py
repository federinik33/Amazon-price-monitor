# import required files and modules
import requests
from bs4 import BeautifulSoup
import pyautogui as pag
import time
import datetime

def check_price(budget,link):
  
	# Function Trova

	def trova(stringa, matrice):
		for i in reversed(range(len(matrice))):
			if stringa in matrice[i]:
	    			return i

	# set the headers and user string
	headers = {
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
	}

	# send a request to fetch HTML of the page
	response=(requests.get(link, headers=headers))

	# create the soup object
	soup=(BeautifulSoup(response.content, 'html.parser'))
	
	# change the encoding to utf-8
	soup.encode('utf-8')
	#print(soup)

	# function to check if the price has dropped
	product_title = soup.find(id= "productTitle")
	if product_title is not None:
		title = product_title.get_text()
	else:
		title = "Nome non trovato"
	soup=str(soup)

	x=soup.find('<span class="a-offscreen">')
	if x is not None:
		price=soup[x+26:x+26+5]
		price = price.replace(',', '.').replace('€', '').replace(' ', '').strip()
	else:
		price='9999999'
	if(price=="ltIE" or price==''):
		price='9999999'
	else:
		print(title.strip())
		print(price)
		print("\n")
	
	
	#converting the string amount to float
	converted_price = float(price)
	if(converted_price < budget):
		print("sceso di prezzo")
		pag.alert(text="sceso di prezzo", title=title)
	"""
	else:
		print("Non è sceso di prezzo")
	"""

	#Se il prezzo è stato trovato lo registra in un file
	if(product_title is not None):
		f = open("Prezzi.txt", "r")
		linea=[]
		cont=0
		k=2000
		for x in f:
			linea.append(x)
			cont+=1
		f.close()
		k=trova(title.strip(),linea)
		if(k==None or linea[k]!= (title.strip()+"\t\t\t"+price+"\n")):
			x = datetime.datetime.now()
			#Crea un file per ogni articolo e ne registra le variazioni di prezzo
			g = open(title.strip().replace('/'," ")+".txt", "a")
			g.write(price+"\t"+x.strftime("%d/%m/%y %X")+"\n")
			g.close()
	#Tiene aggiornati gli ultimi prezzi di tutti gli articoli
		if(k!=None):
		    linea[k]=title.strip()+"\t\t\t"+price+"\n"
		else:
		    linea.append(title.strip()+"\t\t\t"+price+"\n")
		f = open("Prezzi.txt", "w")
		for j in linea:
		    f.write(j)
		f.close()
