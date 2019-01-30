from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
                                        PasswordChangeView,
                                        PasswordResetView,
                                        PasswordResetDoneView,
                                        PasswordResetConfirmView,
                                        PasswordResetCompleteView
                                    )
from .views import register, home, profile, edit_profile

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit-profile'),
    path('password/change/',
         PasswordChangeView.as_view(template_name='accounts/change_password.html',
                                    success_url=reverse_lazy('login')),
         name='change-pw'),
    path('password/reset/',
         PasswordResetView.as_view(template_name='accounts/password_reset.html',
                                   success_url = reverse_lazy('password-reset-done'),
                                   email_template_name='accounts/password_reset_email.html',
                                   subject_template_name='accounts/password_reset_subject.txt',
                                   ),
         name='password-reset'),
    path('password/reset/done/',
         PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password-reset-done'),
    path('password/reset/confirm/<uidb64>/<token>',
         PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',
                                          success_url=reverse_lazy('password-reset-complete'),
                                          ),
         name='password-reset-confirm'),
    path('password/reset/complete/',
         PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password-reset-complete'),
]