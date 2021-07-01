from django.contrib import admin
from .models import Profile,Equipment,EquipmentRental,Human_Resource,Purchase,ServiceRequest,Report

# Register your models here.
admin.site.register(Profile)
admin.site.register(Equipment)
admin.site.register(EquipmentRental)
admin.site.register(Human_Resource)
admin.site.register(Purchase)
admin.site.register(ServiceRequest)
admin.site.register(Report)

