from datetime import datetime
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import login, authenticate
from rest_framework.authentication import TokenAuthentication

from rest_framework import viewsets, generics
from .models import User
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return UserSerializer
        elif self.action == 'create' or self.action == 'update' or self.action == 'partial_update': 
            return UserCreateSerializer
    
    def perform_update(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
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
                is_active = False,
                is_superuser = False,
                is_staff = False
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
    if user is not None:
        #login(request, user)
        return Response({'error':'Usuário logado com sucesso'}, status=status.HTTP_200_OK)
    return Response({'error': 'Usuário ou senha incorretos'}, status=status.HTTP_401_UNAUTHORIZED)

