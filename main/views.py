from django.http import HttpResponse
import json
import threading
from django.shortcuts import render
from .recharge import recharge
from .index import getLuckyMoney
from .models import users
lock = threading.Lock()

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def help(request):
    return render(request, 'help.html')

def index(request):
    return HttpResponse("done")
    req = json.loads(request.body)
    response = getLuckyMoney(req['url'],req['lucky_number'],req['qq'])
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
        users.objects.create(qq=qq, points=20)
        user = users.objects.get(qq=qq)
    return HttpResponse('您当前的余额为{points}点'.format(points = user.points))

def insertuser(request):
    while True:
        lock.acquire()
        req = json.loads(request.body)
        qq = req['qq']
        phone = req['phone']
        try:
            user = users.objects.get(qq=qq)
            user.phone = phone
            user.save()
            lock.release()
            return HttpResponse("换绑成功")
        except:
            try:

                lock.release()
                return HttpResponse("绑定成功")
            except:
                lock.release()
                return HttpResponse("绑定失败")