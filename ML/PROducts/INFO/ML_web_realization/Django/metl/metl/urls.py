"""
URL configuration for metl project.

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

#внутри этого файла мы можем отслеживать различные url-адреса

from django.contrib import admin
from django.urls import path, include #подключаем инклуд

urlpatterns = [
    path('admin/', admin.site.urls), #при переходе по url admin будет открываться приложение admin (в этом случае панель администратора
    path('', include("main.urls")), #отслеживаем главную страницу поэтому пустые кавычки (при переходе на главную страницу деленируем все полномочия main)
]
