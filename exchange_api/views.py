import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from .models import CurrencyData, TodoItem
import requests

# Create your views here.
def home(request):
    # response = requests.get('https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=6&exchange=NASDAQ').json()
    # response = requests.get('https://api.currencyapi.com/v3/latest?apikey=cur_live_9oUc8ZWaSNeL1keeIEXgxxOU4q9PUoyAt0yQU2pQ').json()
    response = CurrencyData.objects.all()
    # return JsonResponse(response)
    return render(request, 'home.html', {'response': response})

def todos(request):
    items = TodoItem.objects.all()
    return render(request, 'todos.html', {"todos": items})

