from rest_framework import serializers


class AddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    street = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    country = serializers.CharField(max_length=255)
    zip = serializers.CharField(max_length=255)


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=255,required=True)
    email = serializers.EmailField(max_length=255,required=True)
    birth_date = serializers.DateField()
    address = AddressSerializer(many=False, read_only=True)
