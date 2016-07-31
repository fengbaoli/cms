# -*- coding: utf-8 -*-
__author__ = '343715'
from django.shortcuts import  render_to_response
from  django.http import HttpResponse
from django.http import  HttpResponseRedirect
from cms.clothescms.models import System_user,User_role,Customer,Seasonal,Brand,Color,Size
from cms.clothescms.models import  Unit,Vip,Category
from django.db import connection,transaction
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session


def usermanger(request):
    if "username" in request.session:
        return render_to_response('usermanger.html')
    else:
        return render_to_response('login.html')


def useradd(request):
    return render_to_response('useradd.html')
def user_result(request):
    addusername = request.POST.get('addusername',None)
    addpassword1 = request.POST.get('addpassword1',None)
    addpassword2 = request.POST.get('addpassword2',None)
    telephone =request.POST.get('telephone',None)
    if addpassword1 != addpassword2:
        message = "两次输入密码不一致，请重新输入"
        return render_to_response('user_passwd_error.html',{'message':message})
    elif System_user.objects.filter(username=addusername):
        message = "用户已经存在，请添加其他用户"
        return render_to_response('user_passwd_error.html',{'message':message})
    else:
        new_user= System_user(username=addusername,password=addpassword1,telephone_number=telephone,user_role_id=1)
        new_user.save()
        message = "添加用户成功"
        return render_to_response('user_passwd_error.html',{'message':message})

def userdel(request):
    return render_to_response('userdel.html')

def user_del_result(request):
    delusername = request.POST.get('delusername',None)
    if not System_user.objects.filter(username=delusername):
        message = "删除的用户不存在"
        return render_to_response('user_passwd_error.html',{'message':message})
    else:
        System_user.objects.filter(username=delusername).delete()
        message = "删除用户成功"
        return render_to_response('user_passwd_error.html',{'message':message})


def modifypass(request):
    return render_to_response('modifypass.html')


def user_mod_result(request):
    oldusername = request.POST.get('oldusername',None)
    oldpassword = request.POST.get('oldpassword',None)
    newpassword = request.POST.get('newpassword',None)
    if not System_user.objects.filter(username=oldusername):
        message = "修改密码用户不存在"
        return render_to_response('user_passwd_error.html',{'message':message})
    p = System_user.objects.get(username=oldusername)
    password = p.password
    if oldpassword!=password:
        message = "旧密码错误，请重新输入"
        return render_to_response('user_passwd_error.html',{'message':message})
    else:
        modifypass_user  = System_user.objects.get(username=oldusername)
        modifypass_user.password =newpassword
        modifypass_user.save()
        message = "修改密码成功"
        return render_to_response('user_passwd_error.html',{'message':message})