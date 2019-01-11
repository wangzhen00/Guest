from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"index.html")

#登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            #return HttpResponse('登录成功')
            auth.login(request,user)#登录
            #response.set_cookie('user',username,3600)#返回cookie添加到浏览器
            request.session['user']=username#添加session信息,请求时添加
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request,'index.html',{'error':'用户名或密码错误'})

#登录成功页面
@login_required
def event_manage(request):
    #username = request.COOKIES.get('user','')#读取cookie
    username = request.session.get('user','')#读取session
    return render(request,"event_manage.html",{"user":username})
    
