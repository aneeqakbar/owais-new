from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "users"

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='RegisterView'),
    path('profile/', views.ProfileView.as_view(), name='ProfileView'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]