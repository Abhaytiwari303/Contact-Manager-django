from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'address']
    search_fields = ['name', 'email', 'phone']
