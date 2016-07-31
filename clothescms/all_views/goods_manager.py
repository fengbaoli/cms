# -*- coding: utf-8 -*-
from django.shortcuts import  render_to_response
from  django.http import HttpResponse
from django.http import  HttpResponseRedirect
from cms.clothescms.models import System_user,User_role,Customer,Seasonal,Brand,Color,Size
from cms.clothescms.models import  Unit,Vip,Category,Goods
from django.db import connection,transaction
from django.contrib.auth.decorators import login_required  
from django.contrib.sessions.models import Session
import MySQLdb
import MySQLdb.cursors
from PIL import Image
import os

#商品管理
def goods_management(request):
    title_sql="select goods_no,goods_type,goods_name,goods_customer,goods_price,goods_discount,goods_after_discount_price,goods_brand,goods_seasonal,goods_quantity,\
goods_images,goods_color,goods_size,purchase_date,exchange_date,sale_status   from clothescms_goods"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('goods_management.html',{'goods':result})

def add_goods(request):
    category_name = Category.objects.all()
    customer_name = Customer.objects.all()
    brand_name = Brand.objects.all()
    seasonal = Seasonal.objects.all()
    unit_name = Unit.objects.all()
    color_name = Color.objects.all()
    size_name = Size.objects.all()
    return render_to_response('add_goods.html',{'goods_type':category_name,'goods_customer':customer_name,'goods_brand':brand_name,'goods_seasonal':seasonal,'goods_unit':unit_name
        ,'goods_color':color_name,'goods_size':size_name})



def addgoods_result(request):
    goods_type = request.POST.get('goods_type',None)
    goods_name = request.POST.get('goods_name',None)
    goods_customer = request.POST.get('goods_customer',None)
    goods_price = request.POST.get('goods_price',None)
    goods_discount = request.POST.get('goods_discount',None)
    goods_brand = request.POST.get('goods_brand',None)
    goods_seasonal = request.POST.get('goods_seasonal',None)
    goods_quantity = request.POST.get('goods_quantity',None)
    goods_unit = request.POST.get('goods_unit',None)
    goods_color = request.POST.get('goods_color',None)
    goods_size = request.POST.get('goods_size',None)
    purchase_date = request.POST.get('purchase_date',None)
    exchange_date = request.POST.get('exchange_date',None)
    sale_status = request.POST.get('sale_status',None)
    goods_no = request.POST.get('goods_no',None)
    #生成goods图片保存名称
    goods_images = goods_no+"_"+goods_name+".jpg"
    #图片保存
    from  clothescms.models import PictureForm
    form = PictureForm(request.POST, request.FILES)
    f = request.FILES["goods_images"]
    # des_origin_path 为你在服务器上保存原始图片的文件物理路径
    des_origin_path =os.getcwd()+"/static/upload/"+goods_images
    #判断图片名是否重复
    des_origin_f = open(des_origin_path, "ab")
    for chunk in f.chunks():
        des_origin_f.write(chunk)
    des_origin_f.close()
    #计算折扣后价格
    goods_after_discount_price = float(goods_price)*float(goods_discount)
    #商品数量
    goods_quantity = goods_quantity+" "+goods_unit
    if  Goods.objects.filter(goods_no = goods_no):
        message = "商品已经存在"
        return render_to_response('goods_err.html',{'message':message})
    else:
        new_goods= Goods(goods_no = goods_no,goods_type = goods_type,goods_name = goods_name,goods_customer = goods_customer,goods_price = goods_price,
        goods_discount = goods_discount,goods_after_discount_price=goods_after_discount_price,goods_brand=goods_brand,goods_seasonal=goods_seasonal,
        goods_quantity=goods_quantity,goods_images=goods_images,goods_color=goods_color,goods_size=goods_size,purchase_date=purchase_date,exchange_date=exchange_date,
        sale_status=sale_status)
        new_goods.save()
        message = "添加商品成功"
        title_sql="select goods_no,goods_type,goods_name,goods_customer,goods_price,goods_discount,goods_after_discount_price,goods_brand,goods_seasonal,goods_quantity,\
    goods_images,goods_color,goods_size,purchase_date,exchange_date,sale_status   from clothescms_goods"
        cursor = connection.cursor()
        cursor.execute(title_sql)
        result  = cursor.fetchall()
        return render_to_response('goods_management.html',{'message':message,'goods':result})

def mod_goods(request):
    goods_no = request.POST.get('goods_no',None)
    title_sql="select goods_no,goods_type,goods_name,goods_customer,goods_price,goods_discount,goods_after_discount_price,goods_brand,goods_seasonal,goods_quantity,\
goods_images,goods_color,goods_size,purchase_date,exchange_date,sale_status   from clothescms_goods where goods_no=%s" %(goods_no)
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('mod_goods.html',{'goods':result})

def modgoods_result(request):
    goods_type = request.POST.get('goods_type',None)
    goods_name = request.POST.get('goods_name',None)
    goods_customer = request.POST.get('goods_customer',None)
    goods_price = request.POST.get('goods_price',None)
    goods_discount = request.POST.get('goods_discount',None)
    goods_brand = request.POST.get('goods_brand',None)
    goods_seasonal = request.POST.get('goods_seasonal',None)
    goods_quantity = request.POST.get('goods_quantity',None)
    goods_unit = request.POST.get('goods_unit',None)
    goods_color = request.POST.get('goods_color',None)
    goods_size = request.POST.get('goods_size',None)
    purchase_date = request.POST.get('purchase_date',None)
    exchange_date = request.POST.get('exchange_date',None)
    sale_status = request.POST.get('sale_status',None)
    goods_no = request.POST.get('goods_no',None)
    goods_after_discount_price = float(goods_price)*float(goods_discount)
    print(goods_after_discount_price)
    #更新
    Goods.objects.filter(goods_no=goods_no).update(goods_price=goods_price,goods_discount=goods_discount,goods_after_discount_price=goods_after_discount_price,goods_quantity=goods_quantity,purchase_date=purchase_date,exchange_date=exchange_date,sale_status=sale_status)
    title_sql="select goods_no,goods_type,goods_name,goods_customer,goods_price,goods_discount,goods_after_discount_price,goods_brand,goods_seasonal,goods_quantity,\
goods_images,goods_color,goods_size,purchase_date,exchange_date,sale_status   from clothescms_goods"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('goods_management.html',{'goods':result})