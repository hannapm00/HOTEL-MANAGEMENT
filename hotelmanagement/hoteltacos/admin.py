from django.contrib import admin
from .models import chef,staff,reservation,outsideuser

# Register your models here.

admin.site.register(chef)
admin.site.register(staff)
admin.site.register(reservation)
admin.site.register(outsideuser)