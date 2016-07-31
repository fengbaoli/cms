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


def unit_management(request):
    title_sql="select unit_no,unit_name from clothescms_unit"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('unit_management.html',{'units':result})
def add_unit(request):
    return render_to_response('add_unit.html')

def addunit_result(request):
    unit_no = request.POST.get('unit_no',None)
    unit_name   = request.POST.get('unit_name',None)
    if  Unit.objects.filter(unit_no=unit_no):
        message = "单位已经存在"
        return render_to_response('unit_err.html',{'message':message})
    new_unit= Unit(unit_no=unit_no,unit_name=unit_name)
    new_unit.save()
    message = "添加单位成功"
    title_sql="select unit_no,unit_name from clothescms_unit"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('unit_management.html',{'message':message,'units':result})
