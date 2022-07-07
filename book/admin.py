from django.contrib import admin
from .models import Contact, Category

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','last_name','category','phone','email','create_date','show')
    list_display_links = ['name', 'last_name']
    search_fields = ['id', 'name','last_name','category__name']
    list_editable = ['phone','show']

admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)