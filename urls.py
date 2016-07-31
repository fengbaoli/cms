# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from cms.clothescms import views
from  cms.clothescms.all_views import user_manager,customer_manager,seasonal_manager,brand_manager,color_manager,size_manager
from cms.clothescms.all_views import unit_manager,vip_manager,category_manager,goods_manager
import os,settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^cms/', include('cms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', views.login),
    url(r'^index/', views.index),
    url(r'^select/', views.select),
    url(r'^logout/', views.logout),
    url(r'^pie/',views.pie),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    #用户管理
    url(r'^usermanager/', user_manager.usermanger),
    url(r'^useradd/', user_manager.useradd),
    url(r'^userdel/', user_manager.userdel),
    url(r'^modifypass/',user_manager.modifypass),
    url(r'^user_del_result/', user_manager.user_del_result),
    url(r'^user_mod_result/',user_manager.user_mod_result),
    url(r'^user_result/', user_manager.user_result),
    #供应商管理
    url(r'^add_customer/',customer_manager.add_customer),
    url(r'^addcustomer_result/', customer_manager.addcustomer_result),
    url(r'^customer_manager/',customer_manager.customer_manager),
    #静态路径
    url(r'^images/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.join( settings.STATIC_PATH , 'images' )}) ,
    url(r'^css/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.join(settings.STATIC_PATH ,'css' )}) ,
    url(r'^js/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.join(settings.STATIC_PATH ,'js' )}) ,
    url(r'^upload/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.join(settings.STATIC_PATH ,'upload' )}) ,
    url(r'^usertemplates/(?P<path>.*)','django.views.static.serve',{'document_root':os.path.join(settings.BASE_DIR,'cms/clothescms/templates/user_manager')}),


    #季节管理
    url(r'^seasonal_management/',seasonal_manager.seasonal_management),
    url(r'^add_seasonal/',seasonal_manager.add_seasonal),
    url(r'^addseasonal_result/',seasonal_manager.addseasonal_result),


    #品牌管理
    url(r'^brand_management/',brand_manager.brand_management),
    url(r'^add_brand/',brand_manager.add_brand),
    url(r'^addbrand_result/',brand_manager.addbrand_result),


    #颜色管理
    url(r'^color_management/',color_manager.color_management),
    url(r'^add_color/',color_manager.add_color),
    url(r'^addcolor_result/',color_manager.addcolor_result),

    #尺码管理
    url(r'^size_management/',size_manager.size_management),
    url(r'^add_size/',size_manager.add_size),
    url(r'^addsize_result/',size_manager.addsize_result),

    #单位管理
    url(r'^unit_management/',unit_manager.unit_management),
    url(r'^add_unit/',unit_manager.add_unit),
    url(r'^addunit_result/',unit_manager.addunit_result),

    #vip管理
    url(r'^vip_management/',vip_manager.vip_management),
    url(r'^add_vip/',vip_manager.add_vip),
    url(r'^addvip_result/',vip_manager.addvip_result),

    #类别管理
    url(r'^category_management/',category_manager.category_management),
    url(r'^add_category/',category_manager.add_category),
    url(r'^addcategory_result/',category_manager.addcategory_result),
    #商品管理
    url(r'^goods_management/',goods_manager.goods_management),
    url(r'^add_goods/',goods_manager.add_goods),
    url(r'^addgoods_result/',goods_manager.addgoods_result),
    url(r'^mod_goods/',goods_manager.mod_goods),
    url(r'^modgoods_result/',goods_manager.modgoods_result),
)

