from drf_standardized_errors.openapi import AutoSchema as DrfStandardizedAutoSchema
from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import generics
from room_services.models import RoomService
from room_services.serializers import RoomServiceSerializer


@extend_schema(
    request=RoomServiceSerializer,
    examples=[
        OpenApiExample(
            'Request Example',
            value={
                'service_name': 5,
                'description': 'Service Description',
                'scheduled_at': '2001/01/01 12:00:00',
                'cost_price': '99.99'
            },
            request_only=True
        ),
        OpenApiExample(
            'Response Example',
            value={
                'service_name': 5,
                'description': 'Service Description',
                'scheduled_at': '2001/01/01 12:00:00',
                'cost_price': '99.99',
                'created_at': '2001/01/01 12:00:00',
                'updated_at': '2001/01/01 12:00:00'
            },
            response_only=True
        ),
    ]
)
class RoomServiceLisCreateView(generics.ListCreateAPIView):
    queryset = RoomService.objects.all().order_by('id')
    serializer_class = RoomServiceSerializer
    schema = DrfStandardizedAutoSchema()

class RoomServiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomService.objects.all().order_by('id')
    serializer_class = RoomServiceSerializer
    schema = DrfStandardizedAutoSchema()
