from django.urls import path
from .views import cycle_list

app_name = 'foaming_kr_api'

urlpatterns = [
    path("", cycle_list, name="cycle_list"),
]
