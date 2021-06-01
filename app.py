import time

from flask import Flask, g
from flask import render_template, redirect, url_for
from flask import request

app = Flask(__name__)


@app.route('/newTab.html', methods=['GET'])
def new_tab():
    error = None
    return render_template('newTab.html', error=error)


@app.route('/list', methods=['GET'])
def get_special_pager_list():
    if request.args is None:
        return {'error': 2, 'code': 200, 'msg': '缺少必要参数'}
    queryMode = ""
    tabId = 0
    content = "服务端的数据"
    # 假装做耗时操作，比如数据库查询等
    time.sleep(3)
    if request.args.get('queryMode') is not None:
        queryMode = str(request.args.get('queryMode'))
    if request.args.get('id') is not None:
        tabId = int(request.args.get('id'))
    if request.args.get('size') is not None:
        size = int(request.args.get('size'))
    print("请求成功参数   queryMode: " + queryMode + "     id:" + str(tabId))
    return {'error': 0, 'code': 200, 'msg': '请求成功', 'index': tabId, 'content': content}


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
    app.run()
