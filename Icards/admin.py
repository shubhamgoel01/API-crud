from django.contrib import admin
from .models import Add_category, Add_subcategory, Add_icard

# Register your models here.

admin.site.register(Add_category)
admin.site.register(Add_subcategory)
admin.site.register(Add_icard)

