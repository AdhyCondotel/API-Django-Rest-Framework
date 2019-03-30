from django.contrib import admin

# Register your models here.
from .models import User, Tenant, Price, Address, Rate

admin.site.register(User)
admin.site.register(Tenant)
admin.site.register(Price)
admin.site.register(Address)
admin.site.register(Rate)