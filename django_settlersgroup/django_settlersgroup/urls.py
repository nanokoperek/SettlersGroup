from django.contrib import admin
from django.urls import include, path
from settlersgroup_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('settlersgroup_app.urls-app')),
]