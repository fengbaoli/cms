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

def seasonal_management(request):
    title_sql="select seasonal,years from clothescms_seasonal"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('seasonal_management.html',{'seasonals':result})

def add_seasonal(request):
    return render_to_response('add_seasonal.html')

def addseasonal_result(request):
    seasonal = request.POST.get('seasonal',None)
    years = request.POST.get('years',None)
    if  Seasonal.objects.filter(seasonal=seasonal,years=years):
        message = "季节已经存在"
        return render_to_response('seasonal_err.html',{'message':message})
    new_seasonal= Seasonal(seasonal=seasonal,years=years)
    new_seasonal.save()
    message = "添加季节成功"
    title_sql="select seasonal,years from clothescms_seasonal"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('seasonal_management.html',{'message':message,'seasonals':result})