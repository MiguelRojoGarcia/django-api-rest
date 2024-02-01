from django.urls import path

from .views import UserView

urlpatterns = [
    path('users/getusers', UserView.as_view(), name='get_all_users'),
    path('users/createusers', UserView.as_view(), name='create_user'),
    path('users/getusersById/<int:id>', UserView.as_view(), name='get_single_user'),
    path('users/deleteUsersById/<int:id>', UserView.as_view(), name='delete_user'),
    path('users/updateUsersById/<int:id>', UserView.as_view(), name='update_user')
]
