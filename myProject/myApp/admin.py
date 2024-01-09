from django.contrib import admin
from myApp.models import *

class office_User_Display(admin.ModelAdmin):
    list_display=['display_name','email','job_type']

    
admin.site.register(Office_User,office_User_Display)
admin.site.register(task_model)
admin.site.register(Office_Manager_Profile)
admin.site.register(Administrative_Assistant_Profile)
admin.site.register(Executive_Assistant_Profile)
admin.site.register(Receptionist_Profile)