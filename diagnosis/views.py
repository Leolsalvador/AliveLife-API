from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .controller import diagnosisControl
from pdf.models import PDF
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import DiagnosisSerializer, ListDiagnosisSerializer
from .models import Diagnosis
from django.shortcuts import get_object_or_404
from pdf.models import Files
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Q
from django.contrib.auth.models import User


class DiagnosisView(APIView):
    serializer_class = DiagnosisSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary='Gerar Pré-diagnóstico',
        responses={200: DiagnosisSerializer(many=True)})

    def post(self, request, id):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        patient_id  = serializer.validated_data.get('idUser')

        patient = get_object_or_404(User, id=patient_id)

        file_instance = get_object_or_404(Files, id=id)

        file_instance.patient = patient
        file_instance.save()

        pdf_instance = get_object_or_404(PDF, file=file_instance)

        diagnosis_text = diagnosisControl(pdf_instance.text, patient=patient)
    
        diagnosis_instance = Diagnosis.objects.create(
            diagnosis=diagnosis_text,
            Medical=pdf_instance.file.user,
            patient=patient,
            pdf=pdf_instance,
            approved=False
        )

        serializer = ListDiagnosisSerializer(diagnosis_instance)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary='Listar pré-diagnósticos',
        responses={200: ListDiagnosisSerializer(many=True)})

    def get(self, request, id):       
        pdf_instance = get_object_or_404(PDF, id=id)
        
        diagnosis = Diagnosis.objects.filter(
            Q(pdf=pdf_instance) & (Q(Medical=request.user) | Q(patient=request.user))
        )

        if not diagnosis.exists():
            return Response({"detail": "Diagnosis not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ListDiagnosisSerializer(diagnosis, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        diagnosis = get_object_or_404(Diagnosis, id=id, Medical=request.user)
        pdf_instance = diagnosis.pdf

        diagnosis_text = diagnosisControl(pdf_instance.text, patient=diagnosis.patient)

        diagnosis.diagnosis = diagnosis_text
        diagnosis.save()

        serializer = ListDiagnosisSerializer(diagnosis)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def patch(self, request, id):
        diagnosis = get_object_or_404(Diagnosis, id=id, Medical=request.user)

        diagnosis.approved = True
        diagnosis.save()

        serializer = ListDiagnosisSerializer(diagnosis)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
