from django.contrib import admin
from .models import *
from atexit import register

# class cateoryAdmin(admin.ModelAdmin):
#     list_display = ('name','image','description')
# admin.site.register(cateory,cateoryAdmin)

admin.site.register(catagory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)