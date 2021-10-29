from django.contrib import admin

from core.models import Seminar, Date

@admin.register(Seminar)
class SeminarAdmin(admin.ModelAdmin):
    pass

@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    pass