from rest_framework import serializers


class DiagnosisSerializer(serializers.Serializer):
    id = serializers.IntegerField()