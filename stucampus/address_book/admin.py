from django.contrib import admin
from address_book.models import Member,Manager

# Register your models here.
class ManagerAdmin(admin.ModelAdmin):
    	list_display = ('managername','password')

class MemberAdmin(admin.ModelAdmin):
	list_display=('name','grade','sex','department','position','stuID','dormitory','birthday_type','phone_num_long','phone_num_short','is_work','wechat','qq')


admin.site.register(Member,MemberAdmin)
admin.site.register(Manager,ManagerAdmin)