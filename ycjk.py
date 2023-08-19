"""
@Qim出品 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
越城监控兑换_v1.1 仅监控共富专区 发现库存后执行推送
8/19_update 修复bug，优化代码
不支持多账号，企业微信通知 参数脚本内置
cron:0/3 * * * *
抓包 https://promoa.ejiaofei.cn/ShaoXingLogin/VerifyUser 取出cookie，body下的参数
"""

key = ""  # 企业微信推送 webhook 后面的 key，为空则不推送

range_num = 3500 #默认兑换积分高于3500

# 脚本内置参数,请装弹后再开炮
cookie = ""
AccountId = ""
SessionId = ""
sign = ""








import json
import re
import requests
response = requests.get('https://netcut.cn/p/e9a1ac26ab3e543b')
note_content_list = re.findall(r'"note_content":"(.*?)"', response.text)
formatted_note_content_list = [note.replace('\\n', '\n').replace('\\/', '/') for note in note_content_list]
for note in formatted_note_content_list:
    print(note)
if cookie and AccountId and SessionId and sign:
    url = "https://promoa.ejiaofei.cn/ShaoXingLogin/VerifyUser"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; PFGM00 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36;xsb_yuecheng;xsb_yuecheng;1.3.0;native_app',
        'Cookie': cookie
    }

    payload = {
        "AccountId": AccountId,
        "SessionId": SessionId,
        "Sign": sign

    }

    response = requests.post(url, headers=headers, data=payload).json()
    value = response["data"]
    response = requests.post(url=value)
    html_code = response.text

    pattern = r'var SESSIONID = "(.*?)";'
    match = re.search(pattern, html_code)

    if match:
        SESSIONID = match.group(1)
        # print("SESSIONID:", SESSIONID)

        url = "https://jfwechat.chengquan.cn/integralMallOrder/getIntegral"
        headers = {
            'uGRDXsIL': SESSIONID,
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; PFGM00 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36;xsb_yuecheng;xsb_yuecheng;1.3.0;native_app',

        }
        response = requests.post(url, headers=headers).json()

        if response['errorMsg'] == "OK":
            data = response['data']
            print(f"\nSESSIONID:{SESSIONID}---积分余额:[{data}]\n")
        else:
            print(f"获取信息失败{response}")

        url = 'https://jfwechat.chengquan.cn/integralMallUserProduct/getList'

        payload = {
            "pageNumber": "1",
            "pageSize": "10",
            "userCategoryId": "8388",
            "type": "PRODUCT_MODULE"
        }

        response = requests.post(url, headers=headers, data=payload)
        data = response.json()
        rows = data['data']['rows']
        product_dict = {}

        for row in rows:
            product_id = row['id']
            product_name = row['productName']
            consume_integral = row['consumeIntegral']

            product_dict[product_id] = {
                'Product Name': product_name,
                'Product ID': product_id,
                'Consume Integral': consume_integral
            }

        for product_id in product_dict:
            url = 'https://jfwechat.chengquan.cn/integralMallProduct/getInventory'
            data = {
                'productId': str(product_id),
                'propertyList': ''
            }

            response = requests.post(url, headers=headers, data=data)
            data = response.json()
            rows = data['data']

            for row in rows:
                saleable_inventory = row['saleableInventory']

                product_info = product_dict[product_id]

                print(f"ID:[{product_info['Product ID']}] {product_info['Product Name']}")
                print(f"兑换积分:[{product_info['Consume Integral']}]库存:[{saleable_inventory}]")
                print()
                if saleable_inventory == 0:
                    # 库存为0，继续下一个商品
                    continue
                else:
                    if product_info['Consume Integral'] >= range_num:
                        url = "https://jfwechat.chengquan.cn/attribution/selectList"
                        response = requests.post(url, headers=headers).json()
                        if response['errorCode'] == 200:
                            takeId = response['data'][0]['id']
                            url = "https://jfwechat.chengquan.cn/integralMallOrder/entityOrderNow"
                            payload = {
                                'productId': product_info['Product ID'],
                                'exchangeNum': '1',
                                'takeId': takeId,
                                'propertyIdList': '',
                                'propertyList': '%5B%5D'
                            }

                            response = requests.post(url, headers=headers, data=payload)
                            data = response.json()
                            print(data)
                            if key:
                                url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=' + key

                                # 需要推送的消息内容
                                messages = [
                                    f"ID:{product_info['Product ID']} {product_info['Product Name']}\n兑换积分:[{product_info['Consume Integral']}]库存:[{saleable_inventory}]\n{data}\n",
                                ]

                                for message in messages:
                                    # 拼接请求体
                                    data = {
                                        "msgtype": "text",
                                        "text": {
                                            "content": message
                                        }
                                    }
                                    headers = {'Content-Type': 'application/json'}

                                    # 发送POST请求
                                    response = requests.post(url, headers=headers, data=json.dumps(data))

                                    # 打印响应结果
                                    print(response.text)
                            else:
                                print("key为空，不执行推送")

                        else:
                            print("获取收货地址失败，退出")
                    else:
                        print(f"积分小于{range_num}不兑换")
else:
    print("别着急开炮，装弹了吗？")




