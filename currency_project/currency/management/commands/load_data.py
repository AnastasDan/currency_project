from datetime import datetime

from django.core.management.base import BaseCommand
from django.db import IntegrityError, transaction

import requests

from currency.models import CurrencyRate

URL = "https://www.cbr-xml-daily.ru/daily_json.js"


class Command(BaseCommand):
    """Команда Django для сбора курсов валют."""

    help = "Собирает курсы валют с сервиса Центрального Банка"

    def bulk_create_currency_rates(self, model, data):
        """Массовое создание курсов валют на основе данных."""
        new_rates = []
        date = data["Date"].split("T")[0]
        date_corr_format = datetime.strptime(date, "%Y-%m-%d").date()

        for charcode, info in data["Valute"].items():
            new_rate = model(
                charcode=charcode,
                date=date_corr_format,
                rate=info["Value"],
            )
            new_rates.append(new_rate)

        try:
            with transaction.atomic():
                model.objects.bulk_create(new_rates)
            return len(new_rates)

        except IntegrityError as e:
            self.stdout.write(
                self.style.ERROR(f"Ошибка при добавлении данных: {e}")
            )
            return 0

    def handle(self, *args, **kwargs):
        """
        Выполняет запрос к сервису ЦБ для получения курсов валют.
        Сохраняет эти данные в базе данных.
        """
        try:
            response = requests.get(URL)
            data = response.json()

        except requests.exceptions.RequestException as error:
            self.stdout.write(self.style.ERROR(f"Сайт недоступен: {error}"))
            return

        count = self.bulk_create_currency_rates(CurrencyRate, data)
        self.stdout.write(
            self.style.SUCCESS(
                f"Успешно добавлено {count} записей курсов валют."
            )
        )
