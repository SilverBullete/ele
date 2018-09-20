# -*- coding: UTF-8 -*-
import requests
import json
import threading
from .models import cookie
from .models import users

lock = threading.Lock()


def getLuckyMoney(url, lucky_number,qq):
    while True:
        lock.acquire()
        next_lucky = 0  # 判断下一个是否为大包
        lastResidueNum = 16
        errortimes = 0
        cook = cookie()
        try:
            user = users.objects.get(qq=qq)
        except:
            users.objects.create(qq=qq, points=20)
            user = users.objects.get(qq=qq)
        while lastResidueNum >= 0:
            id = cook.getNextId()
            used_times = cookie.objects.get(id=id).used_times
            if next_lucky == 0:
                if used_times >= 5:
                    lock.release()
                    return "小号已用完，还剩{num}个就是大包，抱歉".format(num=lucky_number - lastResidueNum)
                coo = cookie.objects.get(id=id)
                eleme_key = coo.eleme_key
                url_appand = coo.url_appand
                track_id = coo.track_id
                c = coo.cookie
                response = hongbao(url, eleme_key, url_appand, track_id, c, coo.phone)
                if response == "网址错误":
                    lock.release()
                    return "网址错误，此次不扣除点数，请换个链接再来吧"

                try:
                    if len(json.loads(response.text)['promotion_records']) == lucky_number - 1:
                        next_lucky = 1
                        user.points -= 4
                        user.save()
                        lock.release()
                        return '下一个就是大包，请手动领取,余额为{point}'.format(point=user.points)
                    if len(json.loads(response.text)['promotion_records']) >= lucky_number:
                        lock.release()
                        return '大包已被领取,请换个链接再来吧'
                    if len(json.loads(response.text)['promotion_records']) == lastResidueNum:
                        print('error', id)
                        errortimes += 1
                    else:
                        errortimes = 0
                        coo.used_times += 1
                        coo.save()
                    if errortimes == 3:
                        # coo.used_times = 10
                        # coo.save()
                        return '链接有问题，若确定没有问题可选择再次发送尝试'
                        #continue
                except:
                    if response.status_code == 400:
                        coo.used_times += 1
                        coo.save()
                    continue
                lastResidueNum = len(json.loads(response.text)['promotion_records'])


def changePhone(eleme_key, url_appand, phone):
    data = {
        'sign': eleme_key,
        'phone': phone
    }
    requests.put('https://h5.ele.me/restapi/v1/weixin/' + url_appand + '/phone', json.dumps(data))


def hongbao(url, eleme_key, url_appand, track_id, cookie, phone):
    try:
        group_sn = url.split('sn=')[1].split('&')[0]
        platform = eval(url.split('platform=')[1].split('&')[0])
    except:
        return '网址错误'

    data = {
        "method": "phone",
        "group_sn": group_sn,
        "sign": eleme_key,
        "phone": phone,
        "device_id": "",
        "hardware_id": "",
        "platform": platform,
        "track_id": track_id,
        "weixin_avatar": "",
        "weixin_username": "",
        "unionid": "fuck"
    }
    header = {
        'content-type': 'text/plain;charset=UTF-8',
        'cookie': cookie,
        'Host': 'h5.ele.me',
        'origin': 'https://h5.ele.me',
        'referer': 'https://h5.ele.me/hongbao/',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.691.400 QQBrowser/9.0.2524.400)',
    }
    request_url = 'https://h5.ele.me/restapi/marketing/promotion/weixin/' + url_appand
    response = requests.post(request_url, data=json.dumps(data),headers=header)
    return response


def gethongbaodetail(response):
    js = json.loads(response.text)
    return (js['promotion_items'][0]['name'], js['promotion_items'][0]['amount'])
