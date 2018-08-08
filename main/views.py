from django.http import HttpResponse
import json
from django.shortcuts import render
from .recharge import recharge
from .index import getLuckyMoney
from .models import users


# Create your views here.

def index(request):
    req = json.loads(request.body)
    response = getLuckyMoney(req['url'],req['qq'])
    return HttpResponse(response)


def pay(request):
    req = json.loads(request.body)
    content = req['content']
    qq = req['qq']
    response = recharge(content,qq)
    return HttpResponse(response)

def getPoints(request):
    req = json.loads(request.body)
    qq = req['qq']
    try:
        user = users.objects.get(qq=qq)
    except:
        return HttpResponse("请先绑定手机号码")
    return HttpResponse('您当前的余额为{points}点'.format(points = user.points))

def insertuser(request):
    req = json.loads(request.body)
    qq = req['qq']
    phone = req['phone']
    try:
        user = users.objects.get(qq=qq)
        user.phone = phone
        user.save()
        return HttpResponse("换绑成功")
    except:
        try:
            users.objects.create(qq=qq,phone=phone,points= 20)
            return HttpResponse("绑定成功")
        except:
            return HttpResponse("绑定失败")