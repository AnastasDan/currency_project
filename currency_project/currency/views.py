from datetime import datetime

from django.http import JsonResponse

from .models import CurrencyRate


def rate_view(request):
    """Представление для отображения курса валюты."""
    charcode = request.GET.get("charcode")
    date_str = request.GET.get(
        "date", datetime.now().date().strftime("%Y-%m-%d")
    )

    if not charcode:
        return JsonResponse(
            {"error": "Currency code not specified."}, status=400
        )

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return JsonResponse(
            {"error": "Date must be the correct format YYYY-MM-DD!"},
            status=400,
        )

    try:
        rate = CurrencyRate.objects.get(charcode=charcode, date=date)
    except CurrencyRate.DoesNotExist:
        return JsonResponse(
            {"error": f"Rate for {charcode} on {date} not found."}, status=404
        )

    data = {
        "charcode": rate.charcode,
        "date": rate.date.strftime("%Y-%m-%d"),
        "rate": rate.rate,
    }
    return JsonResponse(data)
