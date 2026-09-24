from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display=['first_name','username','last_name','email','phone_number','is_active','last_login','date_joined']
    readonly_fields=['date_joined','last_login']
    ordering=['-date_joined']
    filter_horizontal =()
    list_filter =()
    fieldsets =()
admin.site.register(Account,AccountAdmin)
