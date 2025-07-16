from django.urls import path
from store.views.auth_views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
