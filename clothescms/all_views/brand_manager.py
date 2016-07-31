# -*- coding: utf-8 -*-
from django.shortcuts import  render_to_response
from  django.http import HttpResponse
from django.http import  HttpResponseRedirect
from cms.clothescms.models import System_user,User_role,Customer,Seasonal,Brand,Color,Size
from cms.clothescms.models import  Unit,Vip,Category
from django.db import connection,transaction
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
import MySQLdb
import MySQLdb.cursors


def brand_management(request):
    title_sql="select brand_name,brand_des from clothescms_brand"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('brand_management.html',{'brands':result})


def add_brand(request):
    return render_to_response('add_brand.html')


def addbrand_result(request):
    brand_name = request.POST.get('brand_name',None)
    brand_des   = request.POST.get('brand_des',None)
    if  Brand.objects.filter(brand_name=brand_name):
        message = "品牌已经存在"
        return render_to_response('brand_err.html',{'message':message})
    new_brand= Brand(brand_name=brand_name,brand_des=brand_des)
    new_brand.save()
    message = "添加品牌成功"
    title_sql="select brand_name,brand_des from clothescms_brand"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('brand_management.html',{'message':message,'brands':result})

