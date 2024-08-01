from django.urls import path
from roles.views import RoleListCreateView, RoleRetrieveUpdateDestroyView


urlpatterns = [
    path('roles/', RoleListCreateView.as_view(), name='role-list-create'),
    path('roles/<int:pk>/', RoleRetrieveUpdateDestroyView.as_view(), name='role-details'),
]
