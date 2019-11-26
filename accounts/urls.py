from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
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
    path('view_jobs/', views.job_view, name="job_view")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
