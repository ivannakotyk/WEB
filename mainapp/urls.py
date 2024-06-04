from django.urls import path, include
from . import views
from .views import Register

urlpatterns = [
    path('users/', include('django.contrib.auth.urls')),
    path('', views.index_page, name = "home"),
    path('register/', Register.as_view(), name = "register"),
    path('about/', views.about_us, name = "about"),
    path("logout/", views.Logout.as_view(), name="logout"),
]