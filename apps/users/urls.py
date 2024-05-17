from django.urls import path
from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CustomSetPasswordForm

urlpatterns = [
    path('', register, name='register'),
    path('login/', login, name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(form_class=CustomSetPasswordForm), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]

