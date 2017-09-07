from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup



# Create your views here.

def play(request):
    '''
    Ejemplo de como se Scrappear pagina de Gamers y so obtener solo el precio de los videojuegos lo el precio"
    '''
    req = requests.get("https://www.gamershop.com.mx/collections/juegos-ps4?page=2")
    soup = BeautifulSoup(req.text,'html.parser')
    price = soup.find_all('span',attrs={'class':'price_sale'})
    r_price = [p.text for p in price]
    print(r_price)

    #Documentacion de JsonResponse en  https://docs.djangoproject.com/en/1.11/ref/request-response/#jsonresponse-objects
    return JsonResponse(diccionario)


def xbox(request):
    pass
