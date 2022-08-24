from django.contrib import admin
from .models import adminvalid, registerdata,servicedetail,ownermain,delivery
# Register your models here.
admin.site.register(registerdata)
admin.site.register(servicedetail)
admin.site.register(ownermain)
admin.site.register(adminvalid)
admin.site.register(delivery)





