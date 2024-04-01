from django.urls import path
from .views import cycle_list

app_name = 'foaming_kl_api'

urlpatterns = [
    path("", cycle_list, name="cycle_list"),

    # re_path(r"^(?P<date_query>.{10})(?:&(?P<cycle>\d{1}))?/$", cycle_list, name="cycle_list"),
    # re_path(r"^date_query=(?P<date_query>.{10})(?:&cycle=(?P<cycle>\d{1}))?/$", cycle_list, name="cycle_list"),

    # path("<str:date_query>&<str:cycle>/", cycle_list, name="cycle_list"),
    # path("<str:date_query>/", cycle_list, name="cycle_list"),

    # path("date_query=<str:date_query>&cycle=<str:cycle>/", selected_cycle_list, name="selected_cycle_list"),
    # path("date_query=<str:date_query>&cycle=<str:cycle>/", cycle_list, name="cycle_list"),
    # path("date_query=<str:date_query>/", cycle_list, name="cycle_list"),
]
