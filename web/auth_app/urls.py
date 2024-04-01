from django.urls import path
from . import views

app_name = 'auth_app'

urlpatterns = [
    path('login/', views.login_user, name='login_page'),
    path('logout/', views.logout_user, name='logout'),
    path('add_user/', views.add_user, name='add_user_page'),
    path('show_user/', views.show_user, name='show_user_page'),
    path('change_password/', views.change_password, name='change_password_page'),

    path('alert/', views.show_alert, name='alert_page'),
    path('test/', views.test, name='test_page'),
]
