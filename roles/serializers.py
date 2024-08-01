from rest_framework import serializers
from roles.models import Role


class RoleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(required=False, max_length=500)
    created_at = serializers.DateTimeField(read_only=True, format='%Y/%m/%d %H:%M:%S')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y/%m/%d %H:%M:%S')

    def create(self, validated_data):
        return Role.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        if Role.objects.filter(name=value).exists():
            raise serializers.ValidationError("A role with this name already exists.")
        return value
