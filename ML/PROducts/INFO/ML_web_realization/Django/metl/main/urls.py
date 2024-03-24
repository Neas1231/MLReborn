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

from django.urls import path
from . import views #из этой же папки (.) мы импортируем файл views

urlpatterns = [
    path("",views.index), #если пользователь перешел на главную страницу мы должны вызывать определенный метод из файла views
    #path(r"",views.get_data)
]



