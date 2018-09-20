from .models import kami
from .models import users
import threading

lock = threading.Lock()

def recharge(content, qq):
    try:
        user = users.objects.get(qq=qq)
    except:
        users.objects.create(qq=qq, points=20)
        user = users.objects.get(qq=qq)
    while True:
        lock.acquire()
        kamis = kami.objects.filter(used=0)
        num = 0
        for i in kamis:
            if i.kami in content:
                if i.val == 1:
                    i.used = 1
                    i.save()
                    num += 10
                elif i.val == 2:
                    i.used = 1
                    i.save()
                    num += 33
                else:
                    i.used = 1
                    i.save()
                    num += 60
        if num == 0:
            lock.release()
            return None
        else:
            user.points += num
            mon = user.points
            user.save()
            lock.release()
            return "充值成功，充值{num}点，余额为{mon}点".format(num=num,mon=mon)
