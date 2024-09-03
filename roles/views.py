from drf_standardized_errors.openapi import AutoSchema
from rest_framework import generics
from roles.models import Role
from roles.serializers import RoleSerializer

class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    schema = AutoSchema()

    def get_queryset(self):
        queryset = super().get_queryset()

        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class RoleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
