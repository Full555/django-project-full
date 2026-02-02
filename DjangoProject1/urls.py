"""
URL configuration for DjangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import index_pag, MastersView,  AboutViews, ServicesView, MastersHomeView, MasterDetailViews, ServicesByTypeView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('index_pag', index_pag, name="index_pag"),
    path('about', AboutViews.as_view(), name="about"),
    path('index', MastersView.as_view(), name='index'),

    path('sevrice', ServicesView.as_view(), name='service'),

    path('master-home', MastersHomeView.as_view(), name='master-home'),

    path('master-detail/<int:id>/', MasterDetailViews.as_view(), name='master'),

    path('services/type/<int:type_id>/', ServicesByTypeView.as_view(), name='services_by_type'),
    path('accounts/', include('accounts.urls')),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
