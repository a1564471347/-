import requests #line:1
import time #line:2
import random #line:3
import re #line:4
import datetime #line:5
import json #line:6
import os #line:7
from bs4 import BeautifulSoup #line:8
#发现安卓搜索不加积分，今天修复一下
#所需变量：标签页ck、积分任务界面ck、标签页面积分接口请求体里的：apikey、activityID、ocid、user ，还有安卓edge浏览器ck（这个ck我是用的搜索的页面的ck）
#一共就抓仨个包都懒得抓，别来问鼠鼠，问就是鼠鼠懒得回答🥱🥱🥱😅
CK =os .getenv ("WRTFCK")#line:10
pointck =CK .split ('#')[0 ]#line:11
taskck =CK .split ('#')[1 ]#line:12
apikey =CK .split ('#')[2 ]#line:13
activityId =CK .split ('#')[3 ]#line:14
ocid =CK .split ('#')[4 ]#line:15
user =CK .split ('#')[5 ]#line:16
azck =CK .split ('#')[6 ]#line:17
az_header ={'user-agent':'Mozilla/5.0 (Linux; Android 12; JEF-AN00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 EdgA/114.0.1823.74','cookie':azck }#line:22
header_task ={"authority":"rewards.bing.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","accept-language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","cache-control":"max-age=0","referer":"https://rewards.bing.com/status/","sec-ch-ua":"\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Microsoft Edge\";v=\"114\"","sec-ch-ua-arch":"\"x86\"","sec-ch-ua-bitness":"\"64\"","sec-ch-ua-full-version":"\"114.0.1823.43\"","sec-ch-ua-full-version-list":"\"Not.A/Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"114.0.5735.110\", \"Microsoft Edge\";v=\"114.0.1823.43\"","sec-ch-ua-mobile":"?0","sec-ch-ua-model":"\"\"","sec-ch-ua-platform":"\"Windows\"","sec-ch-ua-platform-version":"\"15.0.0\"","sec-fetch-dest":"document","sec-fetch-mode":"navigate","sec-fetch-site":"same-origin","sec-fetch-user":"?1","sec-ms-gec":"A86163F699018123081A75D21E1C182E5A9E8FA59676366C6A7762D15DEAC35B","sec-ms-gec-version":"1-114.0.1823.43","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43","x-edge-shopping-flag":"1","cookie":taskck }#line:49
def NR ():#line:51
    global nr #line:53
    nr =requests .get ('https://v1.hitokoto.cn/?c=f&encode=text').text #line:54
params_check ={'apikey':apikey ,'activityId':activityId ,'ocid':ocid ,'cm':'zh-hk','it':'app','user':user ,'scn':'APP_ANON','version':'2',}#line:64
headers_check ={'authority':'assets.msn.com','accept':'*/*','accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6','cache-control':'max-age=0','cookie':pointck ,'origin':'https://ntp.msn.com','referer':'https://ntp.msn.com/','sec-ch-ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-site','traceparent':'00-485b79a1b3614374b2267803d07896e7-fabe4da733cc45ef-00','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43',}#line:82
def point ():#line:84
    O00O00O0OO0O00O00 =requests .get ('https://assets.msn.com/service/News/Users/me/Rewards',params =params_check ,headers =headers_check ).json ()#line:85
    global point #line:86
    point =O00O00O0OO0O00O00 ['profile']['rewardsPoints']#line:87
    print (f'【当前积分】:{point}')#line:88
def point1 ():#line:90
    O0OOO00O00OOOOOO0 =requests .get ('https://assets.msn.com/service/News/Users/me/Rewards',params =params_check ,headers =headers_check ).json ()#line:91
    O0OO0O00O00OO0OOO =O0OOO00O00OOOOOO0 ['profile']['rewardsPoints']#line:92
    O0OOOO00OO0OOO00O =int (O0OO0O00O00OO0OOO )-int (point )#line:93
    print (f'【当前积分】：{O0OO0O00O00OO0OOO}\n【积分增量】：{O0OOOO00OO0OOO00O}')#line:94
def task ():#line:96
    OO00O0O0OOOO0O000 =int (round (time .time ()*1000 ))#line:97
    O0OOO0O0O0OO0OOOO ={"type":"1","X-Requested-With":"XMLHttpRequest","_":OO00O0O0OOOO0O000 }#line:102
    OO0O0O00O0O0000OO =requests .get ("https://rewards.bing.com/api/getuserinfo",headers =header_task ,params =O0OOO0O0O0OO0OOOO ).json ()#line:103
    O00OO000OO00000OO =OO0O0O00O0O0000OO ['dashboard']['morePromotions']#line:104
    O0O00O0O00O00OOOO =len (O00OO000OO00000OO )#line:105
    for O00OO0OO0OOO0OOOO in range (O0O00O0O00O00OOOO ):#line:106
        OOOO00O0O000OO0O0 =OO0O0O00O0O0000OO ['dashboard']['morePromotions'][O00OO0OO0OOO0OOOO ]['description']#line:107
        O0OOO0O00O00000OO =OO0O0O00O0O0000OO ['dashboard']['morePromotions'][O00OO0OO0OOO0OOOO ]['destinationUrl']#line:108
        OO0O00O00O0000000 =OO0O0O00O0O0000OO ['dashboard']['morePromotions'][O00OO0OO0OOO0OOOO ]['complete']#line:109
        O000000000OOOO000 =OO0O0O00O0O0000OO ['dashboard']['morePromotions'][O00OO0OO0OOO0OOOO ]['hash']#line:110
        O0000OOO0O00OO000 =OO0O0O00O0O0000OO ['dashboard']['morePromotions'][O00OO0OO0OOO0OOOO ]['offerId']#line:111
        print (f'【任务名】：{OOOO00O0O000OO0O0}\n【状态】：{OO0O00O00O0000000}')#line:113
        if not OO0O00O00O0000000 :#line:114
            O000OOOOOO00O000O ={"id":O0000OOO0O00OO000 ,"hash":O000000000OOOO000 ,"timeZone":"480","activityAmount":"1","dbs":"0","__RequestVerificationToken":Token }#line:122
            OO00OO0OOO0000O00 ={"X-Requested-With":"XMLHttpRequest"}#line:125
            requests .post ('https://rewards.bing.com/api/reportactivity',headers =header_task ,params =OO00OO0OOO0000O00 ,data =O000OOOOOO00O000O )#line:126
            print ('正在打搅，马上好🥵')#line:127
            time .sleep (random .randint (2 ,5 ))#line:128
        else :#line:129
            print ('该任务已完成，打完搅然后进行下一次打搅')#line:130
            time .sleep (random .randint (2 ,5 ))#line:131
def bing ():#line:133
    OOO00OO000OOOO0OO =['bing','bing+ai','bing+search','bing+map','bing+image']#line:134
    for OOO0OOO0OOOOO0000 in OOO00OO000OOOO0OO :#line:135
        OO0OO00O0OOO00OOO =OOO00OO000OOOO0OO .index (OOO0OOO0OOOOO0000 )#line:136
        OO0OO00O0OOO00OOO =OO0OO00O0OOO00OOO +1 #line:137
        O0O0O00OOO0O0OOOO =f'https://cn.bing.com/search?q={OOO0OOO0OOOOO0000}&qs=HS&pq=unico&sc=10-5&cvid=A88A9174C5F6477C9E49C5FDA7C6D6A2&FORM=QBRE&sp=1&lq=0'#line:138
        requests .get (url =O0O0O00OOO0O0OOOO ,headers =header_task )#line:139
        OO0O000O0O0O0OOO0 =datetime .datetime .now ().strftime ("%Y-%m-%d %H:%M:%S")#line:142
        print (f'{OO0O000O0O0O0OOO0} bing搜索 【{OO0OO00O0OOO00OOO}/{5}】')#line:143
        time .sleep (random .randint (3 ,6 ))#line:144
def pc ():#line:146
    for O0O00000O00OOOOOO in range (40 ):#line:147
        NR ()#line:148
        O000O0OOOOO0O0OO0 =f'https://cn.bing.com/search?q={nr}&qs=n&form=QBRE&sp=-1&lq=0&pq=%E8%AF%86%E5%88%AB&sc=10-2&sk=&cvid=D332602D4BCC43758A91098E9A12187A&ghsh=0&ghacc=0&ghpl=https://cn.bing.com/search?q=%E8%AF%86%E5%88%AB&qs=n&form=QBRE&sp=-1&lq=0&pq=%E8%AF%86%E5%88%AB&sc=10-2&sk=&cvid=D332602D4BCC43758A91098E9A12187A&ghsh=0&ghacc=0&ghpl='#line:149
        requests .get (url =O000O0OOOOO0O0OO0 ,headers =header_task )#line:151
        OOO0OO0OOOO00O0OO =datetime .datetime .now ().strftime ("%Y-%m-%d %H:%M:%S")#line:152
        O0OOO000O0000O00O =O0O00000O00OOOOOO +1 #line:153
        print (f'{OOO0OO0OOOO00O0OO} pc端搜索：【{O0OOO000O0000O00O}/{40}】\n{nr}')#line:154
        time .sleep (random .randint (3 ,6 ))#line:155
def az ():#line:157
    for O0OOOOOO000OOO000 in range (30 ):#line:158
        NR ()#line:159
        O0OOOOOO00O000O0O =f'https://cn.bing.com/search?q={nr}&setmkt=zh-CN&PC=EMMX01&form=LBT003&scope=web'#line:160
        requests .get (url =O0OOOOOO00O000O0O ,headers =az_header )#line:161
        O00OOOO00OOO0000O =datetime .datetime .now ().strftime ("%Y-%m-%d %H:%M:%S")#line:162
        OOOO0OOOOOO00OOO0 =O0OOOOOO000OOO000 +1 #line:163
        print (f'{O00OOOO00OOO0000O} 安卓端搜索：【{OOOO0OOOOOO00OOO0}/{20}】\n{nr}')#line:164
        time .sleep (random .randint (3 ,6 ))#line:165
def getToken ():#line:166
    OOOOOOOO00OOOOO00 ="https://rewards.bing.com/"#line:167
    OOOOO0O0O00O0000O =requests .get (OOOOOOOO00OOOOO00 ,headers =header_task )#line:168
    O000OO000000000OO =OOOOO0O0O00O0000O .text #line:169
    O0OOOOOOOO00OOOO0 =BeautifulSoup (O000OO000000000OO ,'html.parser')#line:171
    OO00000000000000O =O0OOOOOOOO00OOOO0 .find_all ('input')#line:172
    for O00O0OOOOO0000000 in OO00000000000000O :#line:173
        if O00O0OOOOO0000000 .get ('name')=='__RequestVerificationToken':#line:174
            global Token #line:175
            Token =O00O0OOOOO0000000 .get ('value')#line:176
            print (f'更新token：\n{Token}')#line:177
if __name__ =="__main__":#line:179
    print (f"==========================================")#line:180
    print (f"===============鼠鼠自用版🥱===============")#line:181
    point ()#line:182
    time .sleep (random .randint (1 ,3 ))#line:183
    getToken ()#line:184
    task ()#line:185
    bing ()#line:186
    pc ()#line:187
    az ()#line:188
    point1 ()#line:189
    print (f"===============打搅去喽🥱===============")#line:190
