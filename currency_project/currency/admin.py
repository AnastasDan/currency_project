from django.contrib import admin

from .models import CurrencyRate


@admin.register(CurrencyRate)
class CurrencyAdmin(admin.ModelAdmin):
    """Администрирование модели CurrencyRate."""

    list_display = ("charcode", "date", "rate")
    list_filter = ("charcode", "date")
    search_fields = ("charcode",)
    list_per_page = 20
