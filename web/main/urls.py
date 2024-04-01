from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index_project_page_view, name='home_page'),
    path('favicon.ico', RedirectView.as_view(url='/static/main/img/favicon.ico'))
]
