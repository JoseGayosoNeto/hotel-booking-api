from django.utils import timezone
from rest_framework import serializers
from room_services.models import RoomService


class RoomServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    service_name = serializers.ChoiceField(required=True, choices=RoomService.ServicesNames.choices)
    description = serializers.CharField(required=False, max_length=500)
    scheduled_at = serializers.DateTimeField(required=True, format='%Y/%m/%d %H:%M:%S', input_formats=['%Y/%m/%d %H:%M:%S'])
    cost_price = serializers.DecimalField(required=True, max_digits=20, decimal_places=2)
    created_at = serializers.DateTimeField(read_only=True, format='%Y/%m/%d %H:%M:%S')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y/%m/%d %H:%M:%S')

    def create(self, validated_data):
        return RoomService.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.service_name = validated_data.get('service_name', instance.service_name)
        instance.description = validated_data.get('description', instance.description)
        instance.scheduled_at = validated_data.get('scheduled_at', instance.scheduled_at)
        instance.cost_price = validated_data.get('cost_price', instance.cost_price)
        instance.save()
        return instance

    def validate_cost_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Cost Price cannot be less than 0.")
        return value

    def validate_scheduled_at(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Schedule Date must be in the future.")
        return value
