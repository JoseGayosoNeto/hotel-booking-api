from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from drf_standardized_errors.openapi import AutoSchema as DrfStandardizedAutoSchema
from rest_framework import generics
from roles.models import Role
from roles.serializers import RoleSerializer


@extend_schema_view(
    get=extend_schema(
        parameters=[
            OpenApiParameter(name='name', type=str, location=OpenApiParameter.QUERY,
                            required=False, description='Filter roles by names or characters.')
        ]
    )
)
class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Role.objects.all().order_by('id')
    serializer_class = RoleSerializer
    schema = DrfStandardizedAutoSchema()

    def get_queryset(self):
        queryset = super().get_queryset()

        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class RoleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    schema = DrfStandardizedAutoSchema()
