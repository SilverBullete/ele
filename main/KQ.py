from cqhttp import CQHttp
import requests
import re
import json
import time

bot = CQHttp(api_root='http://127.0.0.1:5700/',
             access_token='',
             secret='')

s1 = '23:55:00'
s2 = '00:05:00'


@bot.on_message()
def handle_msg(context):
    if not context["sub_type"] == "friend":
        return 0
    # if context['message'] == '帮助':
    #     bot.send(context,
    #              '初次使用请发送要领取大包的手机号码来绑定。\n发送“余额”以查询余额。\n分享链接至此。\n输入“充”以充亻直\n更多信息请加入群聊574317060\n有事请联系管理员QQ:3013176731')
    #
    # elif check_phone_number_format(context['message']):
    #     phone = context['message']
    #     qq = str(context['user_id'])
    #     data = {'phone': phone, 'qq': qq}
    #     response = requests.post('http://182.254.130.138:80/api/add/', json.dumps(data))
    #     if 400 <= response.status_code < 500:
    #         bot.send(context, "请求错误，请再试一次或联系管理员QQ:3013176731解决")
    #     elif 500 <= response.status_code:
    #         bot.send(context, "服务器错误，请联系管理员QQ:3013176731解决")
    #     bot.send(context, response.content.decode('utf-8'))
    #
    # elif context['message'] == '充':
    #     bot.send(context, "点击此链接http://t.cn/RkA7dL4以buy卡密，发送卡密至此即可充亻直")
    #     bot.send(context, "点击此链接http://t.cn/RDbHven用浏览器打开即可领取支~付宝红(●'◡'●)包，或打开支~付宝首页搜索“6876302”")
    #
    # elif context['message'] == '余额':
    #     data = {'qq': str(context['user_id'])}
    #     response = requests.post('http://182.254.130.138:80/api/getpoints/', json.dumps(data))
    #     if 400 <= response.status_code < 500:
    #         bot.send(context, "请求错误，请再试一次或联系管理员QQ:3013176731解决")
    #     elif 500 <= response.status_code:
    #         bot.send(context, "服务器错误，请联系管理员QQ:3013176731解决")
    #     bot.send(context, response.content.decode('utf-8'))

    if context['message'] == '帮助':
        bot.send(context, "分享饿了么链接到此，会自动领取到下个大包，根据提示手动领取大包\n开发不易，发送“donate”赞赏")

    elif context['message'] == 'donate':
        bot.send(context,"进入182.254.130.138/donate/赞赏或者在浏览器打开HTTPS://QR.ALIPAY.COM/FKX03561CSBUWOLU1TDN29赞赏，谢谢:-)")

    elif "吱口令" in context['message']:
        bot.send(context, "当前仅支持从饿了么APP分享的链接哟\n在支~付宝点单的用户可以下载饿了么APP，从订单中分享链接至此")

    elif "url=" in context['message']:
        try:
            url = context['message'].split('url=')[1]
            try:
                lucky_number = eval(context['message'].split('饿了么拼手气，第')[1].split('个')[0])
            except:
                lucky_number = eval(url.split('lucky_number=')[1].split('&')[0])
                if lucky_number == 0:
                    bot.send(context, '您提交的链接可能存在问题，请手动更改链接中的lucky_number以便于识别')
                    return 0
            if url.find('https://url.cn/') == 0:
                if time.strftime('%H:%M:%S', time.localtime(time.time())) < s2 or time.strftime('%H:%M:%S',
                                                                                                time.localtime(
                                                                                                        time.time())) > s1:
                    bot.send(context, '23：55-00：05分系统维护，停止使用')
                else:
                    bot.send(context, '链接提交正常，请稍等片刻，高峰期可能等待时间较长')
                    data = {
                        'url': revertShortLink(url),
                        'lucky_number': lucky_number
                    }
                    response = requests.post('http://182.254.130.138:80/api/', json.dumps(data))
                    if 400 <= response.status_code < 504:
                        bot.send(context, "请求超时，请联系管理员QQ:3013176731")
                    else:
                        bot.send(context, response.content.decode('utf-8'))
                        bot.send(context, "点击此链接http://t.cn/RDbHven用浏览器打开即可领取支~付宝红(●'◡'●)包，或打开支~付宝首页搜索“6876302”")
                    # bot.send(context,
                    #          "近期手机淘宝与饿了么有活动\n1.手机淘宝AR扫王老吉可以领取30-5元红(●'◡'●)包，在手机淘宝内的饿了么点单可与品质联盟红(●'◡'●)包一起使用（两者一起至少减10元）\n2.关注手机淘宝里的饿了么，发送领红(●'◡'●)包即可领取随机红(●'◡'●)包")

            elif url.find('https://h5.ele.me/hongbao/') == 0:
                if time.strftime('%H:%M:%S', time.localtime(time.time())) < s2 or time.strftime('%H:%M:%S',
                                                                                                time.localtime(
                                                                                                        time.time())) > s1:
                    bot.send(context, '23：55-00：05分系统维护，停止使用')
                else:
                    bot.send(context, '链接提交正常，请稍等片刻，高峰期可能等待时间较长')
                    data = {
                        'url': url,
                        'qq': str(context['user_id']),
                        'lucky_number': lucky_number
                    }
                    response = requests.post('http://182.254.130.138:80/api/', json.dumps(data))
                    if 400 <= response.status_code < 504:
                        bot.send(context, "请求超时，请联系管理员QQ:3013176731")
                    else:
                        bot.send(context, response.content.decode('utf-8'))
                        bot.send(context, "点击此链接http://t.cn/RDbHven用浏览器打开即可领取支~付宝红(●'◡'●)包，或打开支~付宝首页搜索“6876302”")
                    # bot.send(context,
                    #          "近期手机淘宝与饿了么有活动\n1.手机淘宝AR扫王老吉可以领取30-5元红(●'◡'●)包，在手机淘宝内的饿了么点单可与品质联盟红(●'◡'●)包一起使用（两者一起至少减10元）\n2.关注手机淘宝里的饿了么，发送领hongbao即可领取随机hongbao")
        except:
            bot.send(context, '请回复“帮助”获得使用方法')
            # data = {
            #     'content': context['message'],
            #     'qq': str(context['user_id'])
            # }
            # response = requests.post('http://182.254.130.138:80/api/pay/', json.dumps(data))
            # if 400 <= response.status_code < 500:
            #     bot.send(context, "请求错误，请再试一次或联系管理员QQ:3013176731解决")
            # elif 500 <= response.status_code:
            #     bot.send(context, "服务器错误，请联系管理员QQ:3013176731解决")
            # if response.status_code == 200:
            #     if response.content == b'None':
            #         bot.send(context, '请回复“帮助”获得使用方法')
            #     else:
            #         bot.send(context, response.content.decode('utf-8'))

    else:
        bot.send(context, '请回复“帮助”获得使用方法')
        # data = {
        #     'content': context['message'],
        #     'qq': str(context['user_id'])
        # }
        # response = requests.post('http://182.254.130.138:80/api/pay/', json.dumps(data))
        # if 400 <= response.status_code < 500:
        #     bot.send(context, "请求错误，请再试一次或联系管理员QQ:3013176731解决")
        # elif 500 <= response.status_code:
        #     bot.send(context, "服务器错误，请联系管理员QQ:3013176731解决")
        # if response.status_code == 200:
        #     if response.content == b'None':
        #         bot.send(context, '请回复“帮助”获得使用方法')
        #     else:
        #         bot.send(context, response.content.decode('utf-8'))


def revertShortLink(url):
    url = url[:-1]
    res = requests.head(url)
    return res.headers.get('location')


def check_phone_number_format(phone):
    pattern = re.compile('^0?(13[0-9]|14[56789]|15[012356789]|166|17[012345678]|18[0-9]|19[89])[0-9]{8}$')
    if_match = pattern.match(phone)
    if if_match:
        return True
    return False


bot.run(host='127.0.0.1', port=8080)
