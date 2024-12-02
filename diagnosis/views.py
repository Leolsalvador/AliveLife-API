from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .controller import diagnosisControl
from pdf.models import PDF
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import DiagnosisSerializer, ListDiagnosisSerializer, UpdateDiagnosisSerializer
from .models import Diagnosis
from django.shortcuts import get_object_or_404
from pdf.models import Files
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Q
from django.contrib.auth.models import User
from users.models import Medico
from Crypto.Cipher import AES
from base64 import b64decode
from Crypto.Util.Padding import unpad
from decouple import config


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

        password = serializer.validated_data.get('password')
        patient_id  = serializer.validated_data.get('idUser')

        encrypted_password = serializer.validated_data.get('password')

        key = config('KEY_CRYPTOGRAPHY').encode()
        iv = config('IV_CRYPTOGRAPHY').encode()

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_password = unpad(cipher.decrypt(b64decode(encrypted_password)), AES.block_size).decode('utf-8')

        user = request.user

        if not user.check_password(decrypted_password):
            return Response({'message': 'Incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)

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
        
        # Filtrar o diagnóstico com base no PDF e no usuário atual
        diagnosis = Diagnosis.objects.filter(
            Q(pdf=pdf_instance) & (Q(Medical=request.user) | Q(patient=request.user))
        )

        if not diagnosis.exists():
            return Response({"detail": "Diagnosis not found."}, status=status.HTTP_404_NOT_FOUND)

        diagnosis_data = []
        for diag in diagnosis:
            Medical = Medico.objects.get(user=diag.Medical)
            diagnosis_data.append({
                "id": diag.id,
                "diagnosis": diag.diagnosis,
                "Medical": diag.Medical.first_name,
                "Medical_last_name": diag.Medical.last_name,
                "CRM": Medical.crm,
                "uf_crm": Medical.uf_crm,
                "patient": diag.patient.first_name,
                "patient_last_name": diag.patient.last_name,
                "pdf": diag.pdf.file.name,
                "approved": diag.approved,
            })

        serializer = ListDiagnosisSerializer(data=diagnosis_data, many=True)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class UpdateDiagnosisView(APIView):
    def put(self, request, pk):
        diagnosis = Diagnosis.objects.get(id=pk)
        serializer = UpdateDiagnosisSerializer(data=request.data)

        if serializer.is_valid():
            diagnosis.diagnosis = serializer.data.get('diagnosis')
            diagnosis.save()

            diagnosis = Diagnosis.objects.get(id=pk)
            serializer = ListDiagnosisSerializer(diagnosis)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
