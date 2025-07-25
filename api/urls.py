
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserRegisterLoginViewSet, GenreViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'genres', GenreViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', UserRegisterLoginViewSet.as_view({'post': 'register'}), name='register'),
    path('auth/login/', UserRegisterLoginViewSet.as_view({'post': 'login'}), name='login'),
]
