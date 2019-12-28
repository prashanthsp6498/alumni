from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout_request, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('fgt_pass/', views.forgot_pass, name='forgot_pass'),
    path('job_post/', views.job_post, name="job_post"),
    path('view_jobs/', views.job_view, name="job_view"),
    path('events/', views.events, name="events"),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name="accounts/password_reset.html"
         ),
         name='password_reset'),
    path('password-reset/done',
         auth_views.PasswordResetDoneView.as_view(
             template_name="accounts/password_reset_done.html"
         ),
         name='password_reset_done'),
    path('password-reset-confirm<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="accounts/password_reset_confirm.html"
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
            ),
         name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
