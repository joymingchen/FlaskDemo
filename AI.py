# encoding:utf-8
import requests
import base64
import cv2 as cv
import pytesseract
import numpy as np
from PIL import Image

'''
通用文字识别（高精度版）
'''


def iter_frames(im):
    try:
        i = 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            if i == 0:
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass


# 图片进行去噪处理
def recognize_text(image):
    # 边缘保留滤波  去噪
    blur = cv.pyrMeanShiftFiltering(image, sp=8, sr=30)
    cv.imshow('dst', blur)
    # 对比度加深
    scale_abs = cv.convertScaleAbs(blur, alpha=1.4, beta=0)
    cv.imshow('abs', scale_abs)

    # 替换黄色
    hsv = cv.cvtColor(scale_abs, cv.COLOR_BGR2HSV)
    # 分别设置HSV颜色空间中，红色、黄色、蓝色、绿色的阈值
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    lower_yellow = np.array([26, 43, 46])
    upper_yellow = np.array([34, 255, 255])
    lower_blue = np.array([100, 43, 46])
    upper_blue = np.array([124, 255, 255])
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])

    # 使用inRange函数获取图像中目标颜色的索引
    mask_red = cv.inRange(hsv, lower_red, upper_red)
    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv.inRange(hsv, lower_green, upper_green)
    mask_yellow = cv.inRange(hsv, lower_yellow, upper_yellow)
    img_mask = np.copy(scale_abs)

    color_1 = [128, 9, 21]
    color_2 = [50, 14, 77]
    color_3 = [61, 154, 124]
    color_4 = [59, 170, 246]

    # 给目标像素赋值
    img_mask[mask_red != 0] = color_1
    img_mask[mask_blue != 0] = color_2
    img_mask[mask_green != 0] = color_3
    img_mask[mask_yellow != 0] = color_4

    cv.imshow('img_mask', img_mask)

    # 灰度图像
    gray = cv.cvtColor(img_mask, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray)

    # 自适应二值化
    local = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow('local', local)

    # 二值化
    ret, binary = cv.threshold(local, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print(f'二值化自适应阈值：{ret}')
    cv.imshow('binary', binary)
    # # 形态学操作  获取结构元素  开操作
    # kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 2))
    # bin1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    # cv.imshow('bin1', bin1)
    # kernel = cv.getStructuringElement(cv.MORPH_OPEN, (2, 3))
    # bin2 = cv.morphologyEx(bin1, cv.MORPH_OPEN, kernel)
    # cv.imshow('bin2', bin2)
    # 逻辑运算  让背景为白色  字体为黑  便于识别
    cv.bitwise_not(binary, binary)
    cv.imshow('binary-image', binary)
    # 保存图片
    cv.imwrite(local_path + upload_file_name, binary)
    # # 识别
    # test_message = Image.fromarray(bin2)
    # text = pytesseract.image_to_string(test_message)
    # print(f'识别结果：{text}')
    cv.waitKey(0)
    cv.destroyAllWindows()


# 获取百度AI的token
def get_token(api_key, secret_key):
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + api_key + '&client_secret=' + secret_key
    response = requests.get(host)
    access_token = ''
    if response.status_code == 200:
        access_token = response.json()['access_token']
        print(access_token)
    else:
        print(response.json()['error_description'])
    return access_token


def request_img(url, access_token, file_path):
    f = open(file_path, 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    request_url = url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.post(request_url, data=params, headers=headers)
    result_str = ''
    if response.status_code == 200:
        try:
            words_result = response.json()['words_result']
            print(words_result)
            number_str = words_result[0]
            result_str = number_str['words']
        except KeyError:
            print(response.json()['error_msg'])
    return result_str


# client_id 为官网获取的AK， client_secret 为官网获取的SK
apiKey = "c04po10UzPyP0sgImVGlvsRo"
secretKey = "ydQsGv9jZkvvkEE2GTFQdVZ29fWdy348"
token = get_token(apiKey, secretKey)

# 通用文字识别
common_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 网络图片识别
web_image_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/webimage"
# 手写识别
hand_write_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting"
# 通用文字识别 标准版
basic_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
# 办公文档识别
office_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/doc_analysis_office"

# 二进制方式打开图片文件
# 本地图片的地址 自行修改
# local_path = 'D:\\PycharmProjects\\FlaskProjects\\test1.gif'
#
# # 将gif图片转成PNG图片
# im = Image.open(local_path)
# for i, frame in enumerate(iter_frames(im)):
#     frame.save('image.png', **frame.info)

local_path = 'D:\\PycharmProjects\\FlaskProjects\\'
local_file_name = 'img.png'
upload_file_name = 'upload.png'

src = cv.imread(local_path + local_file_name)
# 处理图片
recognize_text(src)
# 请求结果
result = request_img(basic_url, token, local_path + upload_file_name)
print(result)
