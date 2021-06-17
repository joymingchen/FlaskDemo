import time

from flask import Flask, g, jsonify, make_response
from flask import render_template, redirect, url_for
from flask import request
from flask_cors import CORS

app = Flask(__name__)


@app.route('/newTab.html', methods=['GET'])
def new_tab():
    error = None
    return render_template('newTab.html', error=error)


# 获取列表数据
@app.route('/list', methods=['GET', 'OPTIONS'])
def get_special_pager_list():
    if request.method == 'GET':
        if request.args is None:
            return {'error': 2, 'code': 200, 'msg': '缺少必要参数'}
        queryMode = ""
        tabId = ""
        tableData = [
            {
                "id": 10000,
                "username": "user-0",
                "sex": "女",
                "city": "城市-0",
                "sign": "签名-0",
                "experience": 255,
                "logins": 24,
                "wealth": 82830700,
                "classify": "作家",
                "score": 57
            },
            {
                "id": 10001,
                "username": "user-1",
                "sex": "男",
                "city": "城市-1",
                "sign": "签名-1",
                "experience": 884,
                "logins": 58,
                "wealth": 64928690,
                "classify": "词人",
                "score": 27
            },
            {
                "id": 10002,
                "username": "user-2",
                "sex": "女",
                "city": "城市-2",
                "sign": "签名-2",
                "experience": 650,
                "logins": 77,
                "wealth": 6298078,
                "classify": "酱油",
                "score": 31
            },
            {
                "id": 10003,
                "username": "user-3",
                "sex": "女",
                "city": "城市-3",
                "sign": "签名-3",
                "experience": 362,
                "logins": 157,
                "wealth": 37117017,
                "classify": "诗人",
                "score": 68
            },
            {
                "id": 10004,
                "username": "user-4",
                "sex": "男",
                "city": "城市-4",
                "sign": "签名-4",
                "experience": 807,
                "logins": 51,
                "wealth": 76263262,
                "classify": "作家",
                "score": 6
            },
            {
                "id": 10005,
                "username": "user-5",
                "sex": "女",
                "city": "城市-5",
                "sign": "签名-5",
                "experience": 173,
                "logins": 68,
                "wealth": 60344147,
                "classify": "作家",
                "score": 87
            },
            {
                "id": 10006,
                "username": "user-6",
                "sex": "女",
                "city": "城市-6",
                "sign": "签名-6",
                "experience": 982,
                "logins": 37,
                "wealth": 57768166,
                "classify": "作家",
                "score": 34
            },
            {
                "id": 10007,
                "username": "user-7",
                "sex": "男",
                "city": "城市-7",
                "sign": "签名-7",
                "experience": 727,
                "logins": 150,
                "wealth": 82030578,
                "classify": "作家",
                "score": 28
            },
            {
                "id": 10008,
                "username": "user-8",
                "sex": "男",
                "city": "城市-8",
                "sign": "签名-8",
                "experience": 951,
                "logins": 133,
                "wealth": 16503371,
                "classify": "词人",
                "score": 14
            },
            {
                "id": 10009,
                "username": "user-9",
                "sex": "女",
                "city": "城市-9",
                "sign": "签名-9",
                "experience": 484,
                "logins": 25,
                "wealth": 86801934,
                "classify": "词人",
                "score": 75
            }
        ]
        keyword = ""
        # 耗时操作，比如数据库查询等
        if request.args.get('queryMode') is not None:
            queryMode = str(request.args.get('queryMode'))
        if request.args.get('id') is not None:
            tabId = str(request.args.get('id'))
        if request.args.get('size') is not None:
            size = int(request.args.get('size'))
        if request.args.get('keyword') is not None:
            keyword = str(request.args.get('keyword'))
        print("请求成功参数   queryMode: " + queryMode + "     id:" + str(tabId) + "     keyword:" + str(keyword))

        # 进行搜索
        if keyword == "":
            tableList = tableData
        else:
            newData = []
            for item in tableData:
                if queryMode == 0:
                    # 精准匹配
                    if str(item["id"]) == keyword:
                        newData.append(item)
                else:
                    # 模糊匹配
                    if (str(item["id"]).find(keyword) != -1) or (str(item["username"]).find(keyword) != -1):
                        newData.append(item)
            tableList = newData
        res = make_response(jsonify({'count': len(tableList), 'code': 0, 'msg': '请求成功', 'list': tableList}))
        res.headers['Access-Control-Allow-Origin'] = '*'
        res.headers['Access-Control-Allow-Method'] = '*'
        res.headers['Access-Control-Allow-Headers'] = '*'

        print("请求返回参数   tableList: " + str(tableList))
        return res


# 获取列表数据
@app.route('/menu', methods=['GET', 'OPTIONS'])
def get_menu():
    if request.method == 'GET':
        if request.args is None:
            return {'error': 2, 'code': 200, 'msg': '缺少必要参数'}
        menu = [
            {
                "title": "首页",
                "id": 1000,
                "icon": " ",
                "spread": True,
                "href": ""
            },
            {
                "title": "一级导航-1",
                "id": 1001,
                "icon": "fa-stop-circle",
                "spread": True,
                "href": "http://www.baidu.com",
                "children": [
                    {
                        "title": "二级导航-21",
                        "id": 2001,
                        "icon": "",
                        "href": "lala.html",
                        "spread": True,
                        "children": [
                            {
                                "title": "三级导航-3211",
                                "id": 3001,
                                "icon": " ",
                                "href": "button.html"
                            },
                            {
                                "title": "三级导航-3212",
                                "id": 3002,
                                "icon": " ",
                                "href": "buttwswon.html"
                            }
                        ]
                    },
                    {
                        "title": "二级导航-22",
                        "id": 2002,
                        "icon": "",
                        "href": "lala.html",
                        "spread": True,
                        "children": [
                            {
                                "title": "三级导航-3221",
                                "id": 3021,
                                "icon": " ",
                                "href": "button.html"
                            },
                            {
                                "title": "三级导航-3222",
                                "id": 3022,
                                "icon": " ",
                                "href": "buttwswon.html"
                            }
                        ]
                    }
                ]
            },
            {
                "title": "一级导航-2",
                "id": 1002,
                "icon": "fa-stop-circle",
                "spread": True,
                "href": "http://www.baidu.com"
            },
            {
                "title": "一级导航-3",
                "id": 1003,
                "icon": "fa-stop-circle",
                "spread": True,
                "href": "http://www.baidu.com"
            },
            {
                "title": "一级导航-4",
                "id": 1004,
                "icon": "fa-stop-circle",
                "spread": True,
                "href": "http://www.baidu.com"
            }
        ]
        res = make_response(jsonify({'count': len(menu), 'code': 0, 'msg': '请求成功', 'data': menu}))
        res.headers['Access-Control-Allow-Origin'] = '*'
        res.headers['Access-Control-Allow-Method'] = '*'
        res.headers['Access-Control-Allow-Headers'] = '*'
        print("请求返回参数   tableList: " + str(menu))
        return res


@app.route('/changeTab', methods=['POST', 'GET'])
def change_tab():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'cool':
            return redirect(url_for('home', username=request.form['username']))
        else:
            error = 'Invalid username/password'
    return render_template('tab.html', error=error)


@app.route('/tab', methods=['GET'])
def splash():
    error = None
    if request.method == 'GET':
        return render_template('tab.html', error=error)


@app.route('/search', methods=['GET'])
def search():
    error = None
    if request.method == 'GET':
        return render_template('search.html', error=error)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'cool':
            return redirect(url_for('home', username=request.form['username']))
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)


@app.route('/home')
def home():
    return render_template('home.html', username=request.args.get('username'))


if __name__ == '__main__':
    app.debug = True
    CORS(app, supports_credentials=True)  # 设置跨域
    app.run()
