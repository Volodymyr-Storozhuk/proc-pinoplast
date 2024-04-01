from django.urls import path
from . import views

app_name = 'forming_kr'

urlpatterns = [
    path('forming_full_kr', views.forming_full, name='forming_full_kr'),
    path('forming_full_3', views.forming_full_3, name='forming_full_3'),
    path('forming_group_typeblock_kr', views.forming_group_by_typebloku, name='forming_group_typeblock_kr'),
    path('forming_group_typeblock_3', views.forming_group_by_typebloku_3, name='forming_group_typeblock_3'),
]
