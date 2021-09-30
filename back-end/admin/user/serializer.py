from rest_framework import serializers
from .models import UserVo as user


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    birth = serializers.CharField()
    email = serializers.CharField()
    address = serializers.CharField()

    class Meta:
        model = user
        fileds = '__all__'

    def create(self, valided_data):
        return user.objects.create(**valided_data)

    def update(self, instance, validad_data):
        user.objects.filter(pk=instance.username).update(**validad_data)