from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *
from . import views
urlpatterns = [
    path('login/',auth_view.LoginView.as_view(),name="login"),
    path('logout/',auth_view.LogoutView.as_view(template_name='registration/logout.html'),name="logout"),
    path('register/',register,name='register'),
    path('profile_update/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('password/',views.password,name='password'),
    path('delete', views.delete, name='delete'),
]