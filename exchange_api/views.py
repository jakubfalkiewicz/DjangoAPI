from django.http import HttpResponseBadRequest, JsonResponse
from exchange_api.serializers import CurrencySerializer
from .models import CurrencyData
import requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
def home(request):
    response = requests.get('https://api.currencyapi.com/v3/latest?apikey=cur_live_9oUc8ZWaSNeL1keeIEXgxxOU4q9PUoyAt0yQU2pQ').json()
    data_parameter = response.get("data", {})
    return JsonResponse(data_parameter)

def get_filtered_currencies(name):
    if name:
        return CurrencyData.objects.filter(code__icontains=name)
    else:
        return CurrencyData.objects.all()

def sort_currencies(currencies, sort_param):
    if sort_param:
        if sort_param.lower() == 'codedesc':
            return currencies.order_by('-code', 'value')
        elif sort_param.lower() == 'valueasc':
            return currencies.order_by('value', 'code')
        elif sort_param.lower() == 'codeasc':
            return currencies.order_by('code', 'value')
        elif sort_param.lower() == 'valuedesc':
            return currencies.order_by('-value', 'code')
    return currencies

@csrf_exempt
def exchangeApi(request, id=0):
    if request.method == 'GET':
        name = request.GET.get('name', None)
        sort_param = request.GET.get('sort', None)

        currencies = get_filtered_currencies(name)
        sorted_currencies = sort_currencies(currencies, sort_param)

        currencies_serializer = CurrencySerializer(sorted_currencies, many=True)
        return JsonResponse(currencies_serializer.data, safe=False)
    else:
        return HttpResponseBadRequest("Invalid Request")