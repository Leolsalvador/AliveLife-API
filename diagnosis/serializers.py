from rest_framework import serializers


class DiagnosisSerializer(serializers.Serializer):
    idUser = serializers.IntegerField()


class ListDiagnosisSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    diagnosis = serializers.CharField()
    Medical = serializers.CharField()
    patient = serializers.CharField()
    pdf = serializers.CharField()
    approved = serializers.BooleanField()


class UpdateDiagnosisSerializer(serializers.Serializer):
    diagnosis = serializers.CharField()