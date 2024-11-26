import os, random, string, re

from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group
from drf_yasg.utils import swagger_auto_schema

from .serializers import LoginSerializer, RegisterSerializer

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode
from decouple import config
from django.contrib.sessions.models import Session
from django.utils import timezone
from datetime import timedelta
from .models import Medico, Paciente
from .controllers import format_date


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
        elif user.groups.filter(name='Atendente').exists():
            user_role = 'Atendente'
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

    def get(self, request):
        formatted_users = []

        medicos = User.objects.filter(medico__isnull=False).select_related('medico')
        pacientes = User.objects.filter(paciente__isnull=False).select_related('paciente')

        for user in medicos:
            medico = user.medico
            user_data = {
                'id': user.id,
                'name': f"{user.first_name} {user.last_name}",
                'username': user.username,
                'email': user.email,
                'status': user.is_active,
                'role': "Médico",
                'additional_info': {
                    'nome': medico.nome,
                    'email': medico.email,
                    'cpf': medico.cpf,
                    'data_nascimento': medico.data_nascimento,
                    'crm': medico.crm,
                    'uf_crm': medico.uf_crm,
                    'status': medico.status,
                }
            }
            formatted_users.append(user_data)

        for user in pacientes:
            paciente = user.paciente
            user_data = {
                'id': user.id,
                'name': f"{user.first_name} {user.last_name}",
                'username': user.username,
                'email': user.email,
                'status': user.is_active,
                'role': "Paciente",
                'additional_info': {
                    'nome': paciente.nome,
                    'email': paciente.email,
                    'cpf': paciente.cpf,
                    'data_nascimento': paciente.data_nascimento,
                }
            }
            formatted_users.append(user_data)

        return Response({'users': formatted_users}, status=status.HTTP_200_OK)


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


class RegisterUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        username = data.get("name", "").lower().replace(" ", "")
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        cpf = data.get("cpf", "")
        formatted_cpf = re.sub(r'\D', '', cpf)
        if len(formatted_cpf) == 11:
            formatted_cpf = f"{formatted_cpf[:3]}.{formatted_cpf[3:6]}.{formatted_cpf[6:9]}-{formatted_cpf[9:]}"
        else:
            return Response(
                {"message": "CPF inválido. Deve conter 11 dígitos."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=data.get("name", ""),
                last_name=data.get("surname", ""),
                email=data.get("email", "")
            )

            if data.get("role") == "Médico":
                Medico.objects.create(
                    user=user,
                    nome=data.get("name", ""),
                    email=data.get("email", ""),
                    cpf=formatted_cpf,
                    data_nascimento=data.get("birthDate", ""),
                    crm=data.get("crm", ""),
                    uf_crm=data.get("ufCrm", "")
                )
                group = Group.objects.get(name="Médico")
            elif data.get("role") == "Paciente":
                Paciente.objects.create(
                    user=user,
                    nome=data.get("name", ""),
                    email=data.get("email", ""),
                    cpf=formatted_cpf,
                    data_nascimento=data.get("birthDate", "")
                )
                group = Group.objects.get(name="Paciente")
            else:
                return Response(
                    {"message": "O campo 'role' precisa ser 'Profissional' ou 'Paciente'."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user.groups.add(group)

            return Response(
                {
                    "message": "Usuário criado com sucesso!",
                    "username": username,
                    "password": password,
                },
                status=status.HTTP_201_CREATED
            )
        except Group.DoesNotExist:
            return Response(
                {"message": f"O grupo relacionado ao papel '{data.get('role')}' não foi encontrado."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"message": f"Erro ao criar usuário: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UpdateUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = User.objects.filter(id=pk).first()
        if user is None:
            return Response(
                {"message": "Usuário não encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )

        if user.groups.filter(name='Médico').exists():
            medico = user.medico
            user_data = {
                'id': user.id,
                'name': f"{user.first_name}",
                'surname': user.last_name,
                'username': user.username,
                'email': user.email,
                'status': user.is_active,
                'role': "Médico",
                'additional_info': {
                    'nome': medico.nome,
                    'email': medico.email,
                    'cpf': medico.cpf,
                    'data_nascimento': format_date(medico.data_nascimento),
                    'crm': medico.crm,
                    'uf_crm': medico.uf_crm,
                }
            }
        elif user.groups.filter(name='Paciente').exists():
            paciente = user.paciente
            user_data = {
                'id': user.id,
                'name': f"{user.first_name}",
                'surname': user.last_name,
                'username': user.username,
                'email': user.email,
                'status': user.is_active,
                'role': "Paciente",
                'additional_info': {
                    'nome': paciente.nome,
                    'email': paciente.email,
                    'cpf': paciente.cpf,
                    'data_nascimento': format_date(paciente.data_nascimento),
                }
            }
        else:
            return Response(
                {"message": "Usuário não possui um papel válido."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(user_data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        user = User.objects.filter(id=pk).first()
        if user is None:
            return Response(
                {"message": "Usuário não encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )

        user.first_name = data.get("name", "")
        user.last_name = data.get("surname", "")
        user.email = data.get("email", "")
        user.save()

        if user.groups.filter(name='Médico').exists():
            medico = user.medico
            medico.nome = data.get("name", "")
            medico.email = data.get("email", "")
            medico.cpf = data.get("cpf", "")
            medico.data_nascimento = data.get("birthDate", "")
            medico.crm = data.get("crm", "")
            medico.uf_crm = data.get("ufCrm", "")
            medico.save()
        elif user.groups.filter(name='Paciente').exists():
            paciente = user.paciente
            paciente.nome = data.get("name", "")
            paciente.email = data.get("email", "")
            paciente.cpf = data.get("cpf", "")
            paciente.data_nascimento = data.get("birthDate", "")
            paciente.save()
        else:
            return Response(
                {"message": "Usuário não possui um papel válido."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return Response(
            {"message": "Usuário atualizado com sucesso!"},
            status=status.HTTP_200_OK
        )

    def delete(self, request, pk):
        user = User.objects.filter(id=pk).first()
        if user is None:
            return Response(
                {"message": "Usuário não encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )

        user.is_active = False
        user.save()

        return Response(
            {"message": "Usuário deletado com sucesso!"},
            status=status.HTTP_200_OK
        )
