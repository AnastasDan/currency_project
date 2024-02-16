from django.db import models


class CurrencyRate(models.Model):
    """Модель для представления курсов валют."""

    charcode = models.CharField(max_length=3, verbose_name="Код валюты")
    date = models.DateField(verbose_name="Дата")
    rate = models.DecimalField(
        max_digits=10, decimal_places=4, verbose_name="Курс"
    )

    class Meta:
        verbose_name = "Курс валюты"
        verbose_name_plural = "Курсы валют"
        unique_together = ("charcode", "date")
        ordering = ("-date", "charcode")

    def __str__(self):
        """Возвращает строковое представление объекта CurrencyRate."""
        return f"{self.charcode} на {self.date}: {self.rate} руб."
