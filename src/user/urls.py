from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
from .forms import LoginForm
urlpatterns = [
    path('register/', views.RegisterView.as_view(),name='register'),
    path('login/', views.login,name='login'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout')
]
