from django.contrib import admin

from . models import Category,Product

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display=['category_name','slug']
    search_fields=['category_name']

class ProductAdmin(admin.ModelAdmin):
    list_display        = ['name','price','stock','is_available','created_date','modified_date']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
