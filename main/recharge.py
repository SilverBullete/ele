from .models import kami
from .models import users


def recharge(content, qq):
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
        return None
    else:
        user = users.objects.get(qq=qq)
        user.points += num
        mon = user.points
        user.save()
        return "充值成功，充值{num}点，余额为{mon}点".format(num=num,mon=mon)
