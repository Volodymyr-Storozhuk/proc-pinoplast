from django.urls import path
from . import views

app_name = 'foaming_kl'

urlpatterns = [
    path('', views.foaming_view, name='foaming'),
    path('line_1', views.foaming_line_1_view, name='foaming_line_1'),
    path('line_2', views.foaming_line_2_view, name='foaming_line_2'),

    path('cycle_0', views.foaming_cycle_0_view, name='foaming_cycle_0'),
    path('line_1_cycle_0', views.foaming_line_1_cycle_0_view, name='foaming_line_1_cycle_0'),
    path('line_2_cycle_0', views.foaming_line_2_cycle_0_view, name='foaming_line_2_cycle_0'),
]
