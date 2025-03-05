from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")

def user_list(request):
    return render(request, "user_list.html")

def user_add(request):
    return render(request, "user_add.html")

def tpl(request):
    name = "韩超"
    roles = ["管理员", "CEO", "保安"]
    user_info = {"name": "郭智", "salary": 100000, 'role':"CTO"}
    data_list = [
        {"name": "郭智", "salary": 100000, 'role':"CTO"},
        {"name": "韩立", "salary": 100000, 'role':"CTO"},
        {"name": "王林", "salary": 100000, 'role':"CTO"}
    ]
    return render(request, "tpl.html", {"n1": name, "n2": roles, "n3": user_info, "n4": data_list})

def news(request):
    # 1. 自己定义数据 2. 去数据库获取数据 3. 爬虫
    # 向地址: https://www.chinaunicom.com.cn/43/menu01/1/news?id=8764a172-0143-4324-b52e-831be9a0afb9 发送请求
    # 需要 python 安装第三方模块 requests
    
    # import requests
    # res = requests.get("https://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2021/11/news")
    # data_list = res.json()
    # print(data_list)
    
    return render(request, "news.html")

def something(request):
    # request 封装的是用户发送过来的所有的请求相关数据
    
    # 1.获取请求方式
    print(request.method)
    
    # 2.在 URL 上传递值
    print(request.GET)
    
    # 3.在请求体中提交数据
    print(request.POST)
    
    # 4.响应 直接返回字符串
    # return HttpResponse("返回内容")
    
    # 5.响应 获取 HTML 的内容， + 渲染（替换） -> 字符串，返回给用户浏览器
    # return render(request, 'something.html', {"title": "来了"})
    
    # 6.响应 让浏览器重定向到其他的页面
    return redirect("https://www.baidu.com")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
        
    # 如果是 POST 请求，获取用户提交的数据
    print(request.POST)
    username = request.POST["user"]
    password = request.POST["pwd"]
    if username == "root" and password == "123":
        # return HttpResponse("登陆成功")
        return redirect("https://www.baidu.com")

    # return HttpResponse("登陆失败")
    return render(request, "login.html", {"error_msg": "用户名或密码错误"})