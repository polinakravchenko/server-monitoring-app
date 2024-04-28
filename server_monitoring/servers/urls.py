from rest_framework.routers import DefaultRouter
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import ServerViewSet

server_list = ServerViewSet.as_view({'get': 'get_servers_by_localization'})

urlpatterns = [
    path('servers/', views.servers, name='servers'),
    path('servers/details/<int:id>', views.details, name='details'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('secure/', views.secure_page, name='secure_page'),
    path('upload/', views.upload_form, name='upload_form'),
    path('upload_csv/', ServerViewSet.as_view({'post': 'upload_csv'}), name='upload_csv'),
    path('servers/get_servers_by_localization/<str:localization>/', server_list, name='get_servers_by_localization'),
]

router = DefaultRouter()
router.register(r'servers', ServerViewSet)

urlpatterns += router.urls
