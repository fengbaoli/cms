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

def size_management(request):
    title_sql="select size_no,size_name from clothescms_size"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('size_management.html',{'sizes':result})


def add_size(request):
    return render_to_response('add_size.html')


def addsize_result(request):
    size_no = request.POST.get('size_no',None)
    size_name   = request.POST.get('size_name',None)
    if  Size.objects.filter(size_no=size_no):
        message = "尺寸已经存在"
        return render_to_response('size_err.html',{'message':message})
    new_size= Size(size_no=size_no,size_name=size_name)
    new_size.save()
    message = "添加尺寸成功"
    title_sql="select size_no,size_name from clothescms_size"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('size_management.html',{'message':message,'sizes':result})