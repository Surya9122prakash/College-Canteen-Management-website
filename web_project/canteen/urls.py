from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from web_project.settings import MEDIA_ROOT, MEDIA_URL
urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('menu',views.menu,name='menu'),
    
]+ static(MEDIA_URL, document_root=MEDIA_ROOT)