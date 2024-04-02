from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('servers/', views.servers, name='servers'),
    path('servers/details/<int:id>', views.details, name='details'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('secure/', views.secure_page, name='secure_page'),
]