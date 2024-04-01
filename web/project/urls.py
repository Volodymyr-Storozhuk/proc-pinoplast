"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('auth_app.urls')),

    path('foaming_kl/', include('foaming_kl.urls', namespace='foaming_kl')),
    path('api/v1/foaming_kl/', include('foaming_kl.urls_api', namespace='foaming_kl_api')),

    path('forming_kl/', include('forming_kl.urls', namespace='forming_kl')),
    # path('api/v1/forming_kl/', include('forming_kl.urls_api', namespace='forming_kl_api')),

    path('foaming_kr/', include('foaming_kr.urls', namespace='foaming_kr')),
    path('api/v1/foaming_kr/', include('foaming_kr.urls_api', namespace='foaming_kr_api')),

    path('forming_kr/', include('forming_kr.urls', namespace='forming_kr')),
    # path('api/v1/forming_kr/', include('forming_kr.urls_api', namespace='forming_kr_api')),
]
