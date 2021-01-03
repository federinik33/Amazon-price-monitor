def check_price(budget,link):

  # import required files and modules
  import requests
  from bs4 import BeautifulSoup
  import pyautogui as pag

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

  # function to check if the price has dropped
  product_title = soup.find(id= "productTitle")
  if product_title is not None:
    title = product_title.get_text()
  else:
    title = "Nome non trovato"

  product_price = soup.find(id="priceblock_ourprice")
  if product_price is not None:
    price = product_price.get_text().replace(',', '.').replace('€', '').replace(' ', '').strip()
  else:
    price= "999999"
    product_price = soup.find(id="priceblock_pospromoprice")
    if product_price is not None:
        price = product_price.get_text().replace(',', '.').replace('€', '').replace(' ', '').strip()
    else:
        price= "999999"


  print(title.strip())
  print(price)

  #converting the string amount to float
  converted_price = float(price[0:5])
  if(converted_price < budget):
    print("sceso di prezzo")
    pag.alert(text="sceso di prezzo", title=title)
  else:
    print("Non è sceso di prezzo")
  print("\n")
