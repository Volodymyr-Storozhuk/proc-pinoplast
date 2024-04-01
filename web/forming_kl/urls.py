from django.urls import path
from . import views

app_name = 'forming_kl'

urlpatterns = [
    path('forming_full_kl', views.forming_full, name='forming_full_kl'),
    path('forming_full_1', views.forming_full_1, name='forming_full_1'),
    path('forming_full_2', views.forming_full_2, name='forming_full_2'),
    path('forming_group_typeblock_kl', views.forming_group_by_typebloku, name='forming_group_typeblock_kl'),
    path('forming_group_typeblock_1', views.forming_group_by_typebloku_1, name='forming_group_typeblock_1'),
    path('forming_group_typeblock_2', views.forming_group_by_typebloku_2, name='forming_group_typeblock_2'),
]
