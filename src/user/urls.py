from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
from .forms import LoginForm,PasswordResetForm,SetResetePasswordForm
urlpatterns = [
    path('register/', views.RegisterView.as_view(),name='register'),
    path('login/', views.login,name='login'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),

    path('passwordreset/', auth_view.PasswordResetView.as_view(template_name='user/password-reset.html', form_class=PasswordResetForm),name='password-reset'),


    path('passwordresetedone/', auth_view.PasswordResetDoneView.as_view(template_name='user/password-reset-done.html'),name='password_reset_done'),


    path('passwordresetconfirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name='user/password-reset-confirm.html',form_class=SetResetePasswordForm),name='password_reset_confirm'),


    path('passwordresetcomplete/', auth_view.PasswordResetCompleteView.as_view(template_name='user/password-reset-complete.html'),name='password_reset_complete'),

]
