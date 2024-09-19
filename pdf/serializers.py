from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()
    name = serializers.CharField()


class DeleteFileSerializer(serializers.Serializer):
    id = serializers.IntegerField()
