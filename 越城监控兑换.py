"""
@Qim出品 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
越城监控兑换_v0.1 仅监控共富专区
不支持多账号，企业微信通知 参数脚本内置

抓包 https://promoa.ejiaofei.cn/ShaoXingLogin/VerifyUser 取出cookie，body下的参数
"""

##################################################自定义参数区域##################################################
cookie = ""
AccountId = ""
SessionId = ""
sign = ""

key = ""  # 企业微信推送 webhook 后面的 key

range = 6000  # 默认低于6000积分不兑换

##################################################源码区域，非维护勿动##################################################
import json
import re

import requests

if not cookie or not AccountId or not SessionId or not sign:
    print("参数不完整，程序未运行。请检查参数是否为空")
else:
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

    response = requests.post(url, headers=headers, data=payload)
    value = response.json()["data"]
    # print(value)

    response = requests.post(url=value)
    html_code = response.text

    pattern = r'var SESSIONID = "(.*?)";'
    match = re.search(pattern, html_code)

    if match:
        SESSIONID = match.group(1)
        # print("SESSIONID:", SESSIONID)
        url = 'https://jfwechat.chengquan.cn/integralMallUserProduct/getList'
        headers = {
            'uGRDXsIL': SESSIONID,
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; PFGM00 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36;xsb_yuecheng;xsb_yuecheng;1.3.0;native_app',

        }

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

        url = 'https://jfwechat.chengquan.cn/integralMallProduct/getInventory'
        headers['Referer'] = 'https://jfwechat.chengquan.cn/integralMall/entityProductDetail?productId=9235'

        for product_id in product_dict:
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
                    if product_info['Consume Integral'] > range:
                        url = "https://jfwechat.chengquan.cn/integralMallOrder/entityOrderNow"
                        payload = {
                            'productId': product_info['Product ID'],
                            'exchangeNum': '1',
                            'takeId': '14937',
                            'propertyIdList': '',
                            'propertyList': '[]'
                        }

                        response = requests.post(url, headers=headers, data=payload)
                        data = response.json()

                        # 处理返回的数据
                        print(data)
                        # 推送
                        # 企业微信机器人Webhook地址
                        url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=' + key

                        # 需要推送的消息内容
                        messages = [
                            f"ID:{product_info['Product ID']} {product_info['Product Name']}\n兑换积分:[{product_info['Consume Integral']}]库存:[{saleable_inventory}]\n{data}\n诺，上面兑换状态！",
                        ]

                        # 循环遍历消息列表，依次执行消息推送操作
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
                            exit()
                    else:
                        print(f"积分小于{range}不兑换")

    else:
        print("No value found for SESSIONID")
