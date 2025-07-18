from django.urls import path
from store.views import user_views

urlpatterns = [
    path('orders/', user_views.UserOrderList.as_view(), name='user-orders'),
    path('returns/', user_views.UserReturnList.as_view(), name='user-returns'),
]
