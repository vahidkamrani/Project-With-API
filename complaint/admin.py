from django.contrib import admin
from .models import Complaint
# Register your models here.


class Complaint_admin(admin.ModelAdmin):
    list_display = ('Name','ID_customer','ID_name','Reason_complaint')
    list_filter = ('created_at',)
    search_fields = ('ID_customer',)
    date_hierarchy ='created_at'
    
    
    
admin.site.register(Complaint,Complaint_admin)