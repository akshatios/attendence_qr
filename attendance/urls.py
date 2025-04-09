from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('scan/', views.qr_scan_view, name='scan'),
    path('logout/', views.logout_view, name='logout'),
]
