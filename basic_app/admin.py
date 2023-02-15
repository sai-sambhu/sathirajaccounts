from django.contrib import admin

# Register your models here.
from basic_app.models import Users, AccountHeads, Records, Cash

         
       
admin.site.register([Users,AccountHeads,Records,Cash])