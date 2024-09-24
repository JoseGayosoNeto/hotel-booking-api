from django.urls import path
from room_services.views import RoomServiceLisCreateView, RoomServiceRetrieveUpdateDestroyView

urlpatterns = [
    path('room_services/', RoomServiceLisCreateView.as_view(), name='room_service-list-create'),
    path('room_services/<int:pk>', RoomServiceRetrieveUpdateDestroyView.as_view(), name='room_service-details'),
]
