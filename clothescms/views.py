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
from all_views.user_manager import  *
from all_views.customer_manager import  *
from all_views.seasonal_manager import *
from all_views.brand_manager import *
from  all_views.color_manager import *
from all_views.size_manager import *
from  all_views.unit_manager import *
from all_views.vip_manager import *
from  all_views.category_manager import *
from all_views.goods_manager import *

def login(request):
    username = request.POST.get('username',None)
    password = request.POST.get('password',None)
    code = request.POST.get('code',None)
    gencode = request.POST.get('gencode',None)
    print code,gencode
    if username:
        ac_list = System_user.objects.filter(username=username)
        for account in ac_list:
            if account.username == username and account.password == password and code == gencode:
                request.session['username'] = username
                return  render_to_response('index.html',{'username':username})
            else: 
                return render_to_response('login.html')
    else: 
        return render_to_response('login.html')
def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return  HttpResponseRedirect("/login/")

def index(request):
    if "username" in request.session:
      db = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'root123', db = 'cms',cursorclass = MySQLdb.cursors.DictCursor)
      cursor = db.cursor()
      cursor.execute('select *  from clothescms_net')
      rs = cursor.fetchall()
      Net_sent=[]
      col_tile=[]
      Net_rpkg=[]
      Net_spkg=[]
      Net_recv=[]
      for x in rs:
          Net_sent.append((x['Net_sent']))
          #Net_sent.append(int(x['Net_sent']))
          col_tile.append((x['col_tile']))
          Net_recv.append((x['Net_recv']))
          Net_spkg.append((x['Net_spkg']))
          Net_rpkg.append((x['Net_rpkg']))
      return render_to_response('index.html',{'Net_sent':Net_sent,'col_tile':col_tile,'Net_recv':Net_recv,'Net_spkg':Net_spkg,'Net_rpkg':Net_rpkg})
    else:
      return render_to_response('login.html')


def select(request):
    title_sql="select book.id, book.title,publisher.name , book.publication_date  from clothescms_book book , clothescms_publisher publisher where book.publisher_id = publisher.id"
    cursor = connection.cursor()
    cursor.execute(title_sql)
    result  = cursor.fetchall()
    return render_to_response('select.html',{'title':result})




def pie(request):
    db = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'root123', db = 'cms',cursorclass = MySQLdb.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute('select *  from clothescms_net')
    rs = cursor.fetchall()
    Net_sent=[]
    col_tile=[]
    Net_rpkg=[]
    Net_spkg=[]
    Net_recv=[]
    for x in rs:
        Net_sent.append((x['Net_sent']))
        #Net_sent.append(int(x['Net_sent']))
        col_tile.append((x['col_tile']))
        Net_recv.append((x['Net_recv']))
        Net_spkg.append((x['Net_spkg']))
        Net_rpkg.append((x['Net_rpkg']))
    print type(Net_sent)
    return render_to_response('pie.html',{'Net_sent':Net_sent,'col_tile':col_tile,'Net_recv':Net_recv,'Net_spkg':Net_spkg,'Net_rpkg':Net_rpkg})






