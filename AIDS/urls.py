"""
URL configuration for SRKR project.

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
# from django.contrib import admin
from django.urls import path
from AIDS import views
from AIDS.views import StuDe
urlpatterns = [
    path('home', views.home, name = 'home'),
    path('products', views.products, name = 'products'),
    path('service', views.service, name = 'service'),
    path('contactus', views.contactus, name = 'contactus'),
    path('aboutus', views.aboutus, name = 'aboutus'),
    path('<pk>/stude', StuDe.as_view(), name = 'stude'),
    path('student',views.student, name = 'student'),
    path('form', views.form,name  = 'form'),
    path('detail/<int:id>', views.detail, name = 'detail'),
    path('update/<int:id>', views.update, name = 'update'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('',views.rit, name = ''),
    path('get1', views.get1, name = 'get1'),
    path('post1', views.post1, name = 'post1'),

    
    path('index', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('blog', views.blog, name = 'blog'),
    path('contact', views.contact, name = 'contact'),
    path('portfolio', views.portfolio, name = 'portfolio'),
    path('blog_single', views.blog_single, name = 'blog_single'),
]
