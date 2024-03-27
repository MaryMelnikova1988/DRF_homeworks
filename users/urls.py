from django.urls import path

from users.apps import UsersConfig
from users.views import UserListAPIView, PaymentListAPIView, UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('list/', UserListAPIView.as_view(), name='user_list'),
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
]
