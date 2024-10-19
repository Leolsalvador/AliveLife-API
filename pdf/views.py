import os
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from .models import Files, PDF
from .serializers import FileSerializer, DeleteFileSerializer
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from .controller import extract_text_from_pdf
from diagnosis.models import Diagnosis


class FileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
            operation_summary='Upload de exames',
            request_body=FileSerializer,
            responses={201: 'Arquivo enviado com sucesso!', 400: 'Dados inválidos.', 403: 'Apenas médicos podem fazer upload de exames.'})

    def post(self, request):
        if not request.user.groups.filter(name='Médico').exists():
            return Response({'error': 'Apenas médicos podem fazer upload de exames.'}, status=status.HTTP_403_FORBIDDEN)
        
        file = request.FILES.get('file')
        name = request.data.get('name')

        if Files.objects.filter(name=name).exists():
            return Response({'message': 'Arquivo já existe'}, status=status.HTTP_400_BAD_REQUEST)
        
        if file and name:
            file_up = Files.objects.create(file=file, name=name, user=request.user, patient=request.user)

            pdf = extract_text_from_pdf(file)
            PDF.objects.create(file=Files.objects.last(), text=pdf)

            return Response({'success': 'Arquivo enviado com sucesso!', 'content': {pdf}, 'id': {file_up.id}}, status=status.HTTP_201_CREATED)
        
        return Response({'error': 'Dados inválidos.'}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
            operation_summary='Listar exames',
            responses={200: FileSerializer(many=True)})

    def get(self, request):
        files = Files.objects.filter(Q(user=request.user) | Q(patient=request.user))

        approved_files = []
        for file in files:
            diagnosis = Diagnosis.objects.filter(pdf__file=file, approved=True)
            if diagnosis.exists():
                approved_files.append(file)

        serializer = FileSerializer(approved_files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        files = Files.objects.filter(Q(user=request.user) & Q(patient=id))

        approved_files = []
        for file in files:
            diagnosis = Diagnosis.objects.filter(pdf__file=file, approved=True)
            if diagnosis.exists():
                approved_files.append(file)

        serializer = FileSerializer(approved_files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
            operation_summary='Deletar exame',
            request_body=DeleteFileSerializer,
            responses={200: 'Arquivo deletado com sucesso!', 400: 'ID inválido.'})

    def delete(self, request, id):
        if id:
            file = Files.objects.filter(id=id).first()
            
            if not request.user.groups.filter(name='Médico').exists():
                return Response({'error': 'Apenas médicos podem fazer upload de exames.'}, status=status.HTTP_403_FORBIDDEN)
            elif file:
                file.delete()
                os.remove(file.file.path)
                return Response({'success': 'Arquivo deletado com sucesso!'}, status=status.HTTP_200_OK)
        
        return Response({'error': 'ID inválido.'}, status=status.HTTP_400_BAD_REQUEST)


class PDFView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
            operation_summary='Visualizar PDF',
            responses={200: 'PDF retornado com sucesso!', 400: 'ID inválido.'})
    
    def get(self, request):
        id = request.query_params.get('id')
        
        if id:
            pdf = PDF.objects.filter(file_id=id).first()

            if pdf and (pdf.file.user == request.user or pdf.file.patient == request.user):
                return Response({'pdf': pdf.text}, status=status.HTTP_200_OK)
        
        return Response({'error': 'ID inválido.'}, status=status.HTTP_400_BAD_REQUEST)
        