from django.contrib import admin
from contact import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    search_fields = 'id', 'name',
    ordering = '-id',

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'phone', 'email',
    ordering = '-id', 
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name', 'email', 'phone',
    list_per_page = 30
    list_max_show_all = 100
    list_editable = 'email',
    list_display_links = 'first_name', 'last_name',