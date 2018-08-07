# -*- coding: UTF-8 -*-
import requests
import json
from .models import cookies
from .models import users


def getLuckyMoney(url, mark):
    user = users.objects.get(mark=mark)
    if user.points <= 0:
        return "余额不足"
    phone = user.phone
    lucky_number = eval(url.split('lucky_number=')[1].split('&')[0])
    next_lucky = 0  # 判断下一个是否为大包
    lastResidueNum = 16
    errortimes = 0
    cook = cookies()
    while lastResidueNum >= 0:
        id = cook.getNextId()
        used_times = cookies.objects.get(id=id).used_times
        if next_lucky == 1:
            if used_times >= 5:
                users.deductPoints(mark, 4)
                return "小号已用完，下个就是大包，可手动领取，谢谢，扣除4点，余额为{points}".format(points=user.points - 4)
            cookie = cookies.objects.get(id=id)
            eleme_key = cookie.eleme_key
            url_appand = cookie.url_appand
            changePhone(eleme_key, url_appand, phone)
            response = hongbao(url, eleme_key, url_appand, phone)
            cookie.used_times += 1
            changePhone(eleme_key, url_appand, cookie.phone)
            cookie.save()
            try:
                (name, amount) = gethongbaodetail(response)
                users.deductPoints(mark, 4)
                return "恭喜你领到{name}大包，金额{amount}元，扣除4点，余额为{points}".format(name=name, amount=amount,
                                                                           points=user.points - 4)
            except:
                users.deductPoints(mark, 4)
                return "你可能到达每日领取上限或者已领取过此链接，下个就是大包，你可以分享给好友或者留至明天手动领取，扣除4点，余额为{points}".format(points=user.points - 4)
        elif next_lucky == 0:
            if used_times >= 5:
                return "小号已用完，还剩{num}个就是大包，此次不扣除点数，抱歉".format(num=lucky_number - lastResidueNum)
            cookie = cookies.objects.get(id=id)
            eleme_key = cookie.eleme_key
            url_appand = cookie.url_appand
            response = hongbao(url, eleme_key, url_appand, cookie.phone)
            if response == "网址错误":
                return "网址错误，此次不扣除点数，请换个链接再来吧"
            try:
                if len(json.loads(response.text)['promotion_records']) == lucky_number - 1:
                    next_lucky = 1
                if len(json.loads(response.text)['promotion_records']) >= lucky_number:
                    return '大包已被领取,此次不扣除点数，请换个链接再来吧'
                if len(json.loads(response.text)['promotion_records']) == lastResidueNum:
                    print('error', id)
                    errortimes += 1
                else:
                    errortimes = 0
                    cookie.used_times += 1
                    cookie.save()
                if errortimes == 3:
                    cookie.used_times = 10
                    cookie.save()
                    # return '链接有问题，此次不扣除点数，若确定没有问题可选择再次发送尝试'
                    continue
            except:
                continue
            lastResidueNum = len(json.loads(response.text)['promotion_records'])
            print(lastResidueNum)


def changePhone(eleme_key, url_appand, phone):
    data = {
        'sign': eleme_key,
        'phone': phone
    }
    print(data)
    requests.put('https://h5.ele.me/restapi/v1/weixin/' + url_appand + '/phone', json.dumps(data))


def hongbao(url, eleme_key, url_appand, phone):
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
        "track_id": "undefined",
        "weixin_avatar": "",
        "weixin_username": "",
        "unionid": "fuck"
    }
    # header = {
    #     'origin': 'https://h5.ele.me',
    #     'referer': 'https://h5.ele.me/hongbao/',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.691.400 QQBrowser/9.0.2524.400)',
    # }
    request_url = 'https://h5.ele.me/restapi/marketing/promotion/weixin/' + url_appand
    response = requests.post(request_url, json.dumps(data))
    # status = req.status_code
    # if 200 <= status < 500:
    return response


def gethongbaodetail(response):
    js = json.loads(response.text)
    return (js['promotion_items'][0]['name'], js['promotion_items'][0]['amount'])



