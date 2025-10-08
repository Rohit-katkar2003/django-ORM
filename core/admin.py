from django.contrib import admin
from core.models import Restaurant , Rating , Sale 

# Register your models here.
admin.site.register(Restaurant) 
admin.site.register(Sale)
admin.site.register(Rating) 

