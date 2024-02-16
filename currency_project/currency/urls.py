from django.urls import path

from currency.views import rate_view

urlpatterns = [path("", rate_view, name="rate")]
