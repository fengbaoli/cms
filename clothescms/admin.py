__author__ = 'liushuang'
from django.contrib import  admin
from cms.clothescms.models import  System_user,User_role,Seasonal,Brand
from cms.clothescms.models import Customer,Color,Size,Unit,Vip,Category,Goods

admin.site.register(User_role)
class System_user_admin(admin.ModelAdmin):
    list_display = ('username',)
admin.site.register(Customer)
admin.site.register(System_user,System_user_admin)
admin.site.register(Seasonal)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Unit)
admin.site.register(Vip)
admin.site.register(Category)

admin.site.register(Goods)