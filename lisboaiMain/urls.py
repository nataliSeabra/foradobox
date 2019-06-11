"""lisboaiMain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from lisboaiMain.core import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/lisboai', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),  
    path('', views.index, name='index'),
    path('categoria/<int:id>', views.pageArticle, name='pageArticle'),
    path('<str:slug>', views.post, name='post'),
    path('about/', views.aboutUs, name='aboutUs'),
    path('contact/', views.contact, name='contact'),
    path('send-email/', views.email, name='email'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = 'Lisboai - Admin'
