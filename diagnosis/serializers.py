from rest_framework import serializers


class DiagnosisSerializer(serializers.Serializer):
    idUser = serializers.IntegerField()
    password = serializers.CharField()


class ListDiagnosisSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    diagnosis = serializers.CharField()
    Medical = serializers.CharField()
    patient = serializers.CharField()
    pdf = serializers.CharField()
    approved = serializers.BooleanField()
    Medical_last_name = serializers.CharField(required=False, allow_blank=True)
    CRM = serializers.CharField(required=False, allow_blank=True)
    uf_crm = serializers.CharField(required=False, allow_blank=True)
    patient_last_name = serializers.CharField(required=False, allow_blank=True)


class UpdateDiagnosisSerializer(serializers.Serializer):
    diagnosis = serializers.CharField()