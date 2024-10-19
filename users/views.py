import os

from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema

from .serializers import LoginSerializer

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode
from decouple import config
from django.contrib.sessions.models import Session
from django.utils import timezone
from datetime import timedelta


class UserView(APIView):
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        operation_description="Post a new question and get the report data",
        request_body=LoginSerializer,
        responses={200: LoginSerializer(many=False)}
    )

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        encrypted_password = serializer.validated_data.get('password')

        key = config('KEY_CRYPTOGRAPHY').encode()
        iv = config('IV_CRYPTOGRAPHY').encode()

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_password = unpad(cipher.decrypt(b64decode(encrypted_password)), AES.block_size).decode('utf-8')

        user = User.objects.filter(username=username).first()
        if user is None:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        elif not user.check_password(decrypted_password):
            return Response({'message': 'Incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)
        
        request.session['user_id'] = user.id
        request.session.set_expiry(999999)
        request.session.save()

        refresh = RefreshToken.for_user(user)

        if user.groups.filter(name='Médico').exists():
            user_role = 'Médico'
        elif user.groups.filter(name='Paciente').exists():
            user_role = 'Paciente'
        else:
            user_role = 'Desconhecido'

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'sessionid': request.session.session_key,
            'user_role': user_role
        }, status=status.HTTP_200_OK)

    
    @staticmethod
    def verify_session(sessionid):
        try:
            session = Session.objects.get(session_key=sessionid)
            if session.expire_date > timezone.now():
                return True
            return False
        except Session.DoesNotExist:
            return False


class VerifyTokenView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response(data={'message': 'Token is valid'}, status=status.HTTP_200_OK)

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Médico').exists()

class IsPatient(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Paciente').exists()

class PatientListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        patients = User.objects.filter(groups__name='Paciente')

        formatted_patients = [
            {
                'name': f"{patient.first_name} {patient.last_name}",
                'avatar': '/path-to-avatar.png',
                'id': f'{patient.id}'
            }
            for patient in patients
        ]


        return Response({'patients': formatted_patients}, status=status.HTTP_200_OK)