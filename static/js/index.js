// == 值比较  === 类型比较 $(id) ---->  document.getElementById(id)
function $(id) {
    return typeof id === 'string' ? document.getElementById(id) : id;
}

// 当页面加载完毕
window.onload = function () {
    // 拿到所有的标题(li标签) 和 标题对应的内容(div)
    var titles = $('tab-header').getElementsByTagName('li');
    var divs = $('tab-content').getElementsByClassName('dom');
    // 判断
    if (titles.length !== divs.length) return;

    var notice = document.getElementById("tab-notice")
    var rule = document.getElementById("tab-rule")
    var perfect = document.getElementById("tab-perfect")
    var credit = document.getElementById("tab-credit")
    var product = document.getElementById("tab-product")
    notice.onclick = function () {
        onClickTab(0)
    }
    rule.onclick = function () {
        onClickTab(1)
    }
    perfect.onclick = function () {
        onClickTab(2)
    }
    credit.onclick = function () {
        onClickTab(3)
    }
    product.onclick = function () {
        onClickTab(4)
    }
    // 遍历
    // for (let i = 0; i < titles.length; i++) {
    //     // 取出li标签
    //     const li = titles[i];
    //     li.id = i;
    //     // 监听鼠标的移动
    //     li.onmousemove = function () {
    //         // changeTab(this.id)
    //     }
    //     //监听点击事件
    //     li.onclick = function () {
    //         if (this.id == 0) {
    //             //不进行请求，直接跳转新页面
    //             window.location.href = "newTab.html";
    //         } else {
    //             //进行get请求，获取到返回数据后进行刷新页面
    //             showLoadingDiv(true)
    //             doGet(this.id)
    //         }
    //     }
    // }
}

function onClickTab(tabId) {
    if (tabId === 0) {
        //不进行请求，直接跳转新页面
        window.location.href = "newTab.html";
    } else {
        //进行get请求，获取到返回数据后进行刷新页面
        showLoadingDiv(true)
        doGet(tabId)
    }
}

/**
 * 进行GET请求
 */
function doGet(id) {
    var url = "http://127.0.0.1:5000/list?queryMode=byId&id=" + id;
    var time = 10000;
    var timeout = false;
    var timer = setTimeout(function () {
        timeout = true;
        request.abort();
    }, time);
    var request = new XMLHttpRequest();//第1步，创建一个request对象
    request.open("GET", url);//第2步，设置请求配置
    request.onreadystatechange = function () {
        if (request.readyState !== 4) {
            // (0)未初始化
            // 此阶段确认XMLHttpRequest对象是否创建，并为调用open()方法进行未初始化作好准备。值为0表示对象已经存在，否则浏览器会报错－－对象不存在。
            // (1)载入
            // 此阶段对XMLHttpRequest对象进行初始化，即调用open()方法，根据参数(method,url,true)完成对象状态的设置。
            // 并调用send()方法开始向服务端发送请求。值为1表示正在向服务端发送请求。
            // (2)载入完成
            // 此阶段接收服务器端的响应数据。但获得的还只是服务端响应的原始数据，并不能直接在客户端使用。
            // 值为2表示已经接收完全部响应数据。并为下一阶段对数据解析作好准备。
            // (3)交互
            // 此阶段解析接收到的服务器端响应数据。
            // 即根据服务器端响应头部返回的MIME类型把数据转换成能通过responseBody、responseText或responseXML属性存取的格式，为在客户端调用作好准备。
            // 状态3表示正在解析数据。
            // (4)完成
            // 此阶段确认全部数据都已经解析为客户端可用的格式，解析已经完成。
            // 值为4表示数据解析完毕，可以通过XMLHttpRequest对象的相应属性取得数据。
            // 概而括之，整个XMLHttpRequest对象的生命周期应该包含如下阶段：
            // 创建－初始化请求－发送请求－接收数据－解析数据－完成
            return;
        }
        if (timeout) {
            window.alert("请求超时");
            showLoadingDiv(false);
            return;
        }
        clearTimeout(timer);//取消定时器
        if (request.status === 200) {
            var json = request.responseText;//获取到json字符串，还需解析
            console.log(json);
            showLoadingDiv(false);
            callback(request.responseText);
        }
    };//第3步，设置请求回调监听
    request.send(null);//第4步，发送请求
}

/**
 * 处理服务器的返回数据
 * @param responseText
 */
function callback(responseText) {
    var json = JSON.parse(responseText);
    console.log("code:" + json['code'] + " index:" + json['index']);
    changeTab(json['index'])
}

/**
 * 改变页面
 * @param index
 */
function changeTab(index) {
    // 拿到所有的标题(li标签) 和 标题对应的内容(div)
    var titles = $('tab-header').getElementsByTagName('li');
    var divs = $('tab-content').getElementsByClassName('dom');
    for (let j = 0; j < titles.length; j++) {
        titles[j].className = '';
        divs[j].style.display = 'none';
    }
    titles[index].className = 'selected';
    divs[index].style.display = 'block';
}


/**
 * 是否展示加载框
 * @param isShow
 */
function showLoadingDiv(isShow) {
    let loading = $('loading');
    loading.style.display = isShow ? 'block' : 'none'
}


/**
 * 获取url传递的参数
 * @param variable
 * @returns {string|boolean}
 */
function getQueryVariable(variable) {
    const query = window.location.search.substring(1);
    const vars = query.split("&");
    for (let i = 0; i < vars.length; i++) {
        const pair = vars[i].split("=");
        if (pair[0] === variable) {
            return pair[1];
        }
    }
    return (false);
}