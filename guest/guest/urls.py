"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from sign import views#导入sign应用views文件

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',views.index),#添加index/路径
    url(r'^login_action/$',views.login_action),#添加登录页面路径
    url(r'^event_manage/$',views.event_manage),#添加登录成功跳转页面
    url(r'^accounts/login/$',views.index),#未登录时强制跳转登录页
    url(r'^$',views.index),
]
