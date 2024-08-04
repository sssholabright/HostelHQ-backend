from django.urls import path
from .views import RegisterUserView, CustomTokenObtainPairView, UserListView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login_user'),
    path('users/', UserListView.as_view(), name='users_list'),
]
