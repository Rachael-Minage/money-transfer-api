from django.contrib import admin
from .models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "account_number", "account_name", "account_type", "balance", "currency", "is_active", "date_created")
    search_fields = ("account_number", "account_name", "account_type")
    list_filter = ("account_type", "currency", "is_active")
    ordering = ("-date_created",)

admin.site.register(Account, AccountAdmin)

