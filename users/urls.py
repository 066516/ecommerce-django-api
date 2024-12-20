# users/urls.py
from django.urls import path
from .views import CreateUserView, UserListView, UserDetailView,UserLoginView,ProtectedView

urlpatterns = [
    path('users', CreateUserView.as_view(), name='create_user'),
    path('users/list', UserListView.as_view(), name='user_list'),
    path('users/<int:user_id>', UserDetailView.as_view(), name='user_detail'),
    path('login',UserLoginView.as_view(),name='login'),
    path('user',ProtectedView.as_view(),name='user')


]
