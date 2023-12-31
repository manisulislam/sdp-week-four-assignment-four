
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("category/", include("category.urls")),
    path("task/", include("task.urls")),
]
urlpatterns += staticfiles_urlpatterns()