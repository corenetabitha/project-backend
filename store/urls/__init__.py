
from django.urls import include, path


urlpatterns = [
    path('auth/', include('store.urls.auth_urls')),
    path('admin/', include('store.urls.admin_urls')),     
]
