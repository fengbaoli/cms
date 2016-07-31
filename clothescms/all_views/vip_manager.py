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


def vip_management(request):
    title_sql="select vip_no,vip_type_name,vip_default_discount  from clothescms_vip"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('vip_management.html',{'vips':result})
def add_vip(request):
    return render_to_response('add_vip.html')
def addvip_result(request):
    vip_no = request.POST.get('vip_no',None)
    vip_type_name   = request.POST.get('vip_type_name',None)
    vip_default_discount = request.POST.get('vip_default_discount',None)
    if  Vip.objects.filter(vip_no=vip_no,vip_type_name=vip_type_name):
        message = "VIP已经存在"
        return render_to_response('vip_err.html',{'message':message})
    new_vip= Vip(vip_no=vip_no,vip_type_name=vip_type_name,vip_default_discount=vip_default_discount)
    new_vip.save()
    message = "添加VIP成功"
    title_sql="select vip_no,vip_type_name,vip_default_discount  from clothescms_vip"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('vip_management.html',{'message':message,'vips':result})
