# encoding:utf-8
import requests
import base64

'''
通用文字识别（高精度版）
'''

# client_id 为官网获取的AK， client_secret 为官网获取的SK
apiKey = "c04po10UzPyP0sgImVGlvsRo"
secretKey = "ydQsGv9jZkvvkEE2GTFQdVZ29fWdy348"
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + apiKey + '&client_secret=' + secretKey
response = requests.get(host)
access_token = ''
if response.status_code == 200:
    access_token = response.json()['access_token']
    print(response.json()['access_token'])
else:
    print(response.json()['error_description'])

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
# 本地图片的地址 自行修改
local_path = 'D:\\PycharmProjects\\FlaskProjects\\test.webp'
f = open(local_path, 'rb')
img = base64.b64encode(f.read())

params = {"image": img}
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response.status_code == 200:
    try:
        result = response.json()['words_result']
        print(result)
        number = result[0]
        print(number['words'])
    except Exception as e:
        print(response.json()['error_msg'])
