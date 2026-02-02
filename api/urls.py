from django.urls import include, path
from drf_yasg.views import get_schema_view

urlpatterns = [
path('estate/', include('api.main.endpoints')),
path('', include('api.yasg')),
path('auth/', include('api.auth.endpoints')),

]