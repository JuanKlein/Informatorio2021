"""info URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from apps.blog2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Blog2/', include('apps.blog2.urls')),
    path('', views.home, name='Home'),
    path('posts', views.posts, name='Posts'),
    path('comentarios', views.comentarios, name='Comentarios'),
    path('contacto', views.contacto, name='Contacto'),
    
]
