from django.db import models
from django.forms import ModelForm
import django.forms as forms


class PictureForm(forms.Form):
    imagefile = forms.ImageField()


class User_role(models.Model):
    role_name = models.CharField(max_length=50)
    def __unicode__(self):
        return  u'%s' % (self.role_name)

class UserroleForm(ModelForm):
    class Meta:
        model = User_role 
        fields = '__all__'

class System_user(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telephone_number = models.CharField(max_length=50)
    user_role= models.ForeignKey(User_role)
    def __unicode__(self):
        return u'%s %s ' % (self.username,self.password)
    class Meta:
        ordering=['username']

class Customer(models.Model):
    customer_name=models.CharField(max_length=50)
    customer_telephone=models.CharField(max_length=50)
    customer_bank_no=models.CharField(max_length=50,blank=True)
    customer_webchat_account=models.CharField(max_length=50,blank=True)
    customer_Alipay =models.CharField(max_length=50,blank=True)
    customer_address=models.CharField(max_length=255)
    def __unicode__(self):
        #return u'%s %s %s ' % (self.customer_name,self.customer_telephone,self.customer_address)
        return u'%s ' % (self.customer_name)
    class Meta:
        ordering=['customer_name']
        

class Net(models.Model):
    col_tile = models.DateTimeField()
    Net_sent = models.CharField(max_length=50)
    Net_recv = models.CharField(max_length=50)
    Net_spkg = models.CharField(max_length=50)
    Net_rpkg = models.CharField(max_length=50)	


class Seasonal(models.Model):
    seasonal = models.CharField(max_length=50)
    years = models.CharField(max_length=50)
    def __unicode__(self):
        return u'%s' % (self.seasonal)
    class Meta:
        ordering=['years']

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    brand_des =  models.CharField(max_length=50,blank=True)
    def __unicode__(self):
        return '%s' % (self.brand_name)
    class Meta:
        ordering=['brand_name']

class Color(models.Model):
    color_no = models.CharField(max_length=50)
    color_name =models.CharField(max_length=50)
    def __unicode__(self):
        return u'%s ' % (self.color_name)
    class Meta:
        ordering=['color_no']
class Size(models.Model):
    size_no = models.CharField(max_length=50)
    size_name = models.CharField(max_length=50)
    def __unicode__(self):
        return u'%s' % (self.size_name)
    class Meta:
        ordering=['size_no']

class Unit(models.Model):
    unit_no = models.CharField(max_length=50)
    unit_name = models.CharField(max_length=50)
    def __unicode__(self):
        return u'%s' % (self.unit_name)
    class Meta:
        ordering=['unit_no']

class Vip(models.Model):
    vip_no =models.CharField(max_length=50)
    vip_type_name =models.CharField(max_length=50)
    vip_default_discount = models.CharField(max_length=50)
    def __unicode__(self):
        return u'%s %s %s ' % (self.vip_no,self.vip_type_name,self.vip_default_discount)
    class Meta:
        ordering=['vip_no']
class Category(models.Model):
    category_no = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50)
    def __unicode__(self):
        return u'%s' % (self.category_name)
    class Meta:
        ordering=['category_no']

class Goods(models.Model):
    goods_no = models.CharField(max_length=50)
    goods_type = models.CharField(max_length=50)
    goods_name  = models.CharField(max_length=50)
    goods_customer  = models.CharField(max_length=50)
    goods_price  = models.CharField(max_length=50)
    goods_discount  = models.CharField(max_length=50)
    goods_after_discount_price  = models.CharField(max_length=50)
    goods_brand  = models.CharField(max_length=50)
    goods_seasonal  = models.CharField(max_length=50)
    goods_quantity  = models.CharField(max_length=50)
    goods_images  = models.CharField(max_length=50)
    goods_color  = models.CharField(max_length=50)
    goods_size  = models.CharField(max_length=50)
    purchase_date = models.DateField()
    exchange_date = models.DateField()
    sale_status  = models.CharField(max_length=50)















