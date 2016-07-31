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

def category_management(request):
    title_sql="select category_no,category_name  from clothescms_category"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('category_management.html',{'categorys':result})
def add_category(request):
    return render_to_response('add_category.html')

def addcategory_result(request):
    category_no = request.POST.get('category_no',None)
    category_name   = request.POST.get('category_name',None)
    if  Category.objects.filter(category_no=category_no,category_name=category_name):
        message = "类别已经存在"
        return render_to_response('category_err.html',{'message':message})
    new_category= Category(category_no=category_no,category_name=category_name)
    new_category.save()
    message = "添加类别成功"
    title_sql="select category_no,category_name  from clothescms_category"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('category_management.html',{'message':message,'categorys':result})
