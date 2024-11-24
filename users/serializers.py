from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField()
    surname = serializers.CharField()
    email = serializers.EmailField()
    cpf = serializers.CharField()
    birthDate = serializers.DateField()
    crm = serializers.CharField(required=False, allow_blank=True)
    ufCrm = serializers.CharField(required=False, allow_blank=True)
    role = serializers.CharField()
