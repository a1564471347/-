import requests,time,re,json,random
from urllib import parse

phone = ['账号1用户名','账号2用户名']#Zepp Life账号，可手机或邮箱
password = ['账号1密码','账号2密码'] #Zepp Life密码
step_min = 30000 #最小步数
step_max = 50000 #最大步数
p_token= '' #push+ token
content=''
for i in range(len(phone)):
    step = str(random.randint(step_min,step_max))
    phone1 = parse.quote_plus(phone[i])
    password1 = password[i]

    response = requests.get(f"https://apis.jxcxin.cn/api/mi?user={phone1}&password={password1}&step={step}")
    print(response.text)

    try:
        aaa = json.loads(response.text)
        if aaa['code'] == '200':
            print(aaa['msg'])
            content = content + f'【账号{i+1}】' + aaa['msg'] + f"，步数：{step}"'\n'
        elif aaa['code'] == '201' :
            content = content + f'【账号{i + 1}】' + aaa['msg'] + '\n'
        else:
            print(aaa['msg'])
            content = content + f'【账号{i+1}】' + aaa['msg'] + '\n'
    except Exception:
        print(response.text)
        content = content + f'【账号{i+1}】失败，运行错误\n'

content = parse.quote_plus(content)  
title = parse.quote_plus('刷步数') 
requests.get(f'http://www.pushplus.plus/send?token={p_token}&title={title}&content={content}%0A%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7%EF%BC%9A%E5%81%B6%E5%B0%94%E6%95%B2%E4%BB%A3%E7%A0%81')

