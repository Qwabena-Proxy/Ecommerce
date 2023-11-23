from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Machine)
admin.site.register(MachineCategory)
admin.site.register(MachineBrand)
admin.site.register(BrandImages)
admin.site.register(Gender)
admin.site.register(FeedBack)