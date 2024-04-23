"""
URL configuration for teleBotMaker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from tradeboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lending/', lending_view, name="lending"),
    path('login/', login_view, name="login"),
    path('registration/', registration_view, name="registration"),
    path('', first_page, name="first-page"),
    path('dashboard/', dashboard_view, name="dashboard"),
    path('settings/', settings_view, name="settings"),
    path('profile/', profile_view, name="profile"),
    path('logout/', logout_view, name="logout"),
]
