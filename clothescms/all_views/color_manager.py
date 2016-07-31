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


def color_management(request):
    title_sql="select color_no,color_name from clothescms_color"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('color_management.html',{'colors':result})
def add_color(request):
    return render_to_response('add_color.html')

def addcolor_result(request):
    color_no = request.POST.get('color_no',None)
    color_name  = request.POST.get('color_name',None)
    if  Color.objects.filter(color_no = color_no):
        message = "颜色已经存在"
        return render_to_response('color_err.html',{'message':message})
    new_color= Color(color_no=color_no,color_name=color_name)
    new_color.save()
    message = "添加颜色成功"
    title_sql="select color_no,color_name from clothescms_color"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('color_management.html',{'message':message,'colors':result})
