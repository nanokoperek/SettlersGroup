from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='settlersgroup-home'),
    path('home/', views.home, name='settlersgroup-home'),
    path('about/', views.about, name='blog-about'),
    path('register/', views.register, name='register')
]

urlpatterns += staticfiles_urlpatterns()