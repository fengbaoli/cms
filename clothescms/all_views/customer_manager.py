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


def customer_manager(request):
    title_sql="select customer_name,customer_telephone,customer_bank_no,customer_webchat_account,customer_Alipay,customer_address from clothescms_customer"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('customer_manager.html',{'customer':result})

def add_customer(request):
    return render_to_response('add_customer.html')

def addcustomer_result(request):
    customer_name = request.POST.get('customer_name',None)
    customer_tel = request.POST.get('customer_tel',None)
    customer_bank_no = request.POST.get('customer_bank_no',None)
    customer_webcat_no =request.POST.get('customer_webcat_no',None)
    customer_Alipay_no = request.POST.get('customer_Alipay_no',None)
    customer_address = request.POST.get('customer_address',None)
    if  Customer.objects.filter(customer_name=customer_name,customer_telephone=customer_tel):
        message = "客户已经存在"
        return render_to_response('customer_err.html',{'message':message})
    new_customer= Customer(customer_name=customer_name,customer_telephone=customer_tel,customer_bank_no=customer_bank_no,customer_webchat_account=customer_webcat_no,customer_Alipay=customer_Alipay_no,customer_address=customer_address)
    new_customer.save()
    message = "添加客户成功"
    title_sql="select customer_name,customer_telephone,customer_bank_no,customer_webchat_account,customer_Alipay,customer_address from clothescms_customer"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    print result
    return render_to_response('customer_manager.html',{'message':message,'customer':result})

