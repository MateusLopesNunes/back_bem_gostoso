from datetime import datetime
from random import choice
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import login, authenticate
from rest_framework.authentication import TokenAuthentication

from rest_framework import viewsets, generics
from .models import User
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import string
from django.core.mail import EmailMessage


#Utils
def generate_password():
    size = 10
    values = string.ascii_letters + string.digits
    new_password = ''
    for i in range(size):
        new_password += choice(values)
    return new_password

def send_email(message, title, user_email):
    to_email = user_email
    email = EmailMessage(
                title, message, to=[to_email]
    )
    email.send()


class UserViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return UserSerializer
        elif self.action == 'create': 
            return UserCreateSerializer
        elif self.action == 'update' or self.action == 'partial_update':
            return UserUpdateSerializer
    
    def perform_update(self, serializer):
        instance = serializer.save()
        instance.updated_at = datetime.now()
        instance.save()

class CreateUser(generics.CreateAPIView):   
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def create(self, request):
        email = User.objects.filter(email=request.data['email'])
        if len(email) == 1:
            return Response({"msg": "Este email já existe no sistema"} ,status=status.HTTP_404_NOT_FOUND)
        
        try:
            data = request.data
            user = User(
                username = data['username'],
                birth_date = data['birth_date'],
                telephone = data['telephone'],
                email = data['email'],
                is_active = True,
                is_superuser = True,
                is_staff = True
            )
            user.set_password(data['password'])
            user.save()

        except:
            return Response({"error": "Erro inesperado"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"msg": "Usuário cadastrado com sucesso"}, status=status.HTTP_201_CREATED) 
    
        
@api_view(['POST'])
def login(request):
    email = request.data['email']
    password = request.data['password']

    user = authenticate(request, email=email, password=password)
    user_id = user.pk
    if user is not None:
        return Response({'msg':'Usuário logado com sucesso', 'userId': user_id }, status=status.HTTP_200_OK)
    return Response({'error': 'Usuário ou senha incorretos'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def reset_password(request):
    email = request.data['email']
    username = request.data['username']

    userByEmail = User.objects.filter(email=email)
    userByUsername = User.objects.filter(username=username)
    
    if userByEmail and userByEmail[0].pk == userByUsername[0].pk:
        user = userByEmail[0]
        new_password = generate_password()
        user.set_password(new_password)
        user.save()

        mail_subject = 'Recuperação de senha'
        message = f'Sua nova senha é: {new_password}'
        send_email(message, mail_subject, user.email)
        return Response({'msg': 'A sua nova senha foi enviada para seu email'}, status=status.HTTP_200_OK)

    return Response({'error': 'Email ou username inválidos'}, status=status.HTTP_400_BAD_REQUEST)
