from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from .models import KKM, Settings, ClientError

admin.site.index_title = "Техническая поддержка сайта по внутреннему телефону 365"
    
@admin.register(KKM)
class KKMAdmin(admin.ModelAdmin):
    list_display = ('reg', 'ser', 'adr', 'exp', 'days')
    search_fields = ['reg', 'name', 'ser', 'adr', 'yl']
    view_on_site = False
    ordering = ('exp',)

    @admin.display(description="Количество дней до срока окончания ФН")
    def days(self, KKM):
        return KKM.days

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    exclude = ('id',)

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

@admin.register(ClientError)
class ErrorsAdmin(admin.ModelAdmin):
    list_display = ('dt', 'name', 'message')
    ordering = ('-dt',)
    search_fields = ['message', 'name']