from django.contrib import admin
from .models import KKM, FN

admin.site.register(KKM)
admin.site.register(FN)
admin.site.site_header = "Контроль фискальных накопителей"
admin.site.site_title = "Контроль фискальных накопителей"
admin.site.index_title = "Техническая поддержка сайта по внутреннему телефону 365"