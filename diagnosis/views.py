from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .controller import diagnosisControl
from pdf.models import PDF
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import DiagnosisSerializer
from .models import Diagnosis
from django.shortcuts import get_object_or_404
from pdf.models import Files
from rest_framework import status


class DiagnosisView(APIView):
    serializer_class = DiagnosisSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        file_id = serializer.validated_data.get('id')

        file_instance = get_object_or_404(Files, id=file_id)

        pdf_instance = get_object_or_404(PDF, file=file_instance)

        diagnosis_text = diagnosisControl(pdf_instance.text, patient=pdf_instance.file.patient)

        diagnosis_instance = Diagnosis.objects.create(
            diagnosis=diagnosis_text,
            Medical=pdf_instance.file.user,
            patient=pdf_instance.file.patient
        )

        return Response({'diagnosis': diagnosis_instance.diagnosis}, status=status.HTTP_201_CREATED)
