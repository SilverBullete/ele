from django.http import HttpResponse
import json
from django.shortcuts import render
from .models import cookies
from .index import getLuckyMoney
from .index import changePhone


# Create your views here.

def index(request):
    req = json.loads(request.body)
    response = getLuckyMoney(req['url'],req['uin'])
    return HttpResponse(response)
    # cookie = cookies.objects.get(id=21)
    # eleme_key = cookie.eleme_key
    # phone = cookie.phone
    # url_appand =cookie.url_appand
    # response = changePhone(eleme_key,url_appand,"17326029758")
    # return HttpResponse(response)

