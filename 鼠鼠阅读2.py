import requests
import time
import hashlib
import random
import os
#变量名SSYDCK  值ck里的gfsessionid、zzbb_info、num用#拼接，num为你想跑的次数
#  行的ck自己替换一下，ck取自阅读的包，域名里有weixin.qq的。阅读的最后一个包的url（以json结尾的那个）替换一下
CK = os.getenv("SSYDCK")
gfsessionid = CK.split('#')[0]
zzbb_info = CK.split('#')[1]
num = int(CK.split('#')[2])
ST = 1

headers = {
    "Host": "2449509.weolb.dajimu.mep00sutqs.cfd",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; JEF-AN00 Build/HUAWEIJEF-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5197 MMWEBSDK/20230504 MMWEBID/4023 MicroMessenger/8.0.37.2380(0x2800255B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "X-Requested-With": "com.tencent.mm",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
cookies = {
    "gfsessionid": gfsessionid,
    "zzbb_info": zzbb_info
}
def CHECK():
    KEY()
    params = {
    "time": t,
    "sign": sign
    }
    res = requests.get("http://2449509.weolb.dajimu.mep00sutqs.cfd/read/info", headers=headers, cookies=cookies, params=params, verify=False).json()
    if 'code' in res and res['code'] == 0:
        read = res['data']['read']
        gold = res['data']['gold']
        remain = res['data']['remain']
        print(f'【状态】：\n[金币]：{gold} [阅读数]：{read} [可提现]:{remain}')
    else:
        print("寄")


def FN():
    KEY()
    header_finish = {
    "Host": "2449509.x3fifwb20.dajimu.wuv68yd1pr.cfd",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; JEF-AN00 Build/HUAWEIJEF-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5197 MMWEBSDK/20230504 MMWEBID/4023 MicroMessenger/8.0.37.2380(0x2800255B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "http://2449509.x3fifwb20.dajimu.wuv68yd1pr.cfd",
    "X-Requested-With": "com.tencent.mm",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = {
    "time": t,
    "sign": sign
    }
    res = requests.post("http://2449509.x3fifwb20.dajimu.wuv68yd1pr.cfd/read/finish", headers=header_finish, cookies=cookies, data=data, verify=False).json()
    #print(res)
    if 'code' in res and res['code'] == 0:
        check = res['data']['check']
        gain = res['data']['gain']
        read = res['data']['read']
        gold = res['data']['gold']
        remain = res['data']['remain']
        print(f'【是否被检测】：{check}\n[获币]：{gain} [金币]：{gold} [阅读数]：{read} [可提现]:{remain} ')
    else:
        print("寄")

def GET():
    KEY()
    params = {
    "time": t,
    "sign": sign
    }
    res = requests.get("http://2449509.x3fifwb20.dajimu.wuv68yd1pr.cfd/read/task", headers=headers, cookies=cookies, params=params, verify=False).json()
    if 'code' in res and res['code'] == 0:
        link = res['data']['link']
        global url0
        url0 = link.split('#')[0]
        time.sleep(random.randint(2, 3))
        READ()
        time.sleep(random.randint(6, 9))
        FN()
        
    else:
        global ST
        ST = 0
        msg = res['message']
        print(msg)


def READ():

    headers = {
    'Host': 'mp.weixin.qq.com',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; JEF-AN00 Build/HUAWEIJEF-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5197 MMWEBSDK/20230504 MMWEBID/4023 MicroMessenger/8.0.37.2380(0x2800255B) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Accept': '*/*',
    'Origin': 'https://mp.weixin.qq.com',
    'X-Requested-With': 'com.tencent.mm',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': f'{url0}&ascene=34&devicetype=android-31&version=2800255b&nettype=WIFI&lang=zh_CN&countrycode=CN&exportkey=n_ChQIAhIQXqxCJgDwviqeSeBcQ%%2BvoihLbAQIE97dBBAEAAAAAAGICEnQLIM8AAAAOpnltbLcz9gKNyK89dVj0Wyy%%2BNGXfgFsYCkhZ6HsGdyBbd6Q4hA1I4WeWbI033TB%%2FV2yc5VlRNatYXlyO%%2BF6lh%%2FRN6%%2FqohhA6LY3Te%%2F1fPCJjp2Zkf2B0QcVy0VZOVps%%2FvRuogf3JblbvJNhr0LnJhbZHggzJD2xQNy7qC6nVtbYbBsIBWC%%2BjPs6t7N0T1EtDpULzLYyiyxWjaK%%2FZkJlbTOT6E7H%%2FCU0BrmPgWtYxuJUYJ9EXAP2tfTeengzCFJa2aeXyGg%%3D%%3D&pass_ticket=O%%2BXcq3O4Za%%2FmoE8YOlbAX2UQ7wEt9Ew3BFqzTKaiExm8ZflEDZOoKmD8ulYhMbS7&wx_header=3',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    #'Cookie': 'rewardsn=; wxtokenkey=777; wxuin=179483292; devicetype=android-31; version=2800255b; lang=zh_CN; appmsg_token=1231_SNl92OmIYkXYocSOtZYfyfVrdRUopqRDEWVyQuc9ViilInvoB24wESPHaWk~; pass_ticket=O+Xcq3O4Za/moE8YOlbAX2UQ7wEt9Ew3BFqzTKaiExm8ZflEDZOoKmD8ulYhMbS7; wap_sid2=CJzlylUStgF5X0hFcTYtSU9tWXY2TXBsUVEtUlhyeEtCRFRvYkFHS2xINXAyQUlhMWpUOXh0RnIyVXBEUmRpcDZkRlJWb2NGRTdhYjlnemVQRld6MDdvSnI3VURJUGY5dkI1Z1pxVkxKZGY1RVE3bWpDT25qaFlST0Z3Nl9RWmFWMEZWazNQSWxVamk1NnZHWWZ4aHpqdUFISW1vRHg4ZUhKajdLOURTNFZGMWJ2RUJZTVNkUm1yQklBQUF+fjCzy/OmBjgNQAE=',
    }
    cookie = {
    'rewardsn': '',
    'wxtokenkey': '               换成你自己的                                         ',
    'wxuin': '              换成你自己的                                        ',
    'devicetype': '              换成你自己的                                        ',
    'version': '              换成你自己的                                        ',
    'lang': 'zh_CN',
    'appmsg_token': '              换成你自己的                                        ',
    'pass_ticket': '              换成你自己的                                        ',
    'wap_sid2': '              换成你自己的                                        ',
    }
    requests.post('换成你自己的url', cookies=cookie, headers=headers)


def KEY():
    global t
    t = int(time.time())
    a = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={t}'
    result = hashlib.sha256(str(a).encode('utf-8')).hexdigest()
    global sign
    sign = result





if __name__ == "__main__":
    print(f"==========================================")
    print(f"===============鼠鼠自用版🥱===============")   
    
    for i in range(num):
        i = i+1
        print(f"===============第{i}打搅===============")
        CHECK()
        time.sleep(random.randint(2, 3))
        GET()
        if ST == 0:
            break

        
    print(f"================打完睡觉🥱================")  

