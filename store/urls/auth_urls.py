from django.urls import path
from store.views.auth_views import RegisterView, CustomTokenObtainPairView  # ✅ use custom view
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # ✅ correct name
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
