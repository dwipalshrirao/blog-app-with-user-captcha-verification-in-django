"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from .views import create_blog,search_blog,single_blog,delete_blog,update_blog
app_name = 'blogapp'

urlpatterns = [
    
    
    path('cblog/', create_blog, name="create_blog"),
    path('sblog/', search_blog, name="search_blog"),
    path('single-blog/<int:id>', single_blog, name="singleblog"),
    path('deleteblog/<int:id>', delete_blog, name="deleteblog"),
    path('updateblog/<int:id>', update_blog, name="updateblog"),
    # path('login/', login_view, name="login"),
    # path('logout/', logout_view, name="logout"),
]
