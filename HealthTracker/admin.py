from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from HealthTracker.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_superuser', 'is_adult', 'is_child')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(Account, AccountAdmin)