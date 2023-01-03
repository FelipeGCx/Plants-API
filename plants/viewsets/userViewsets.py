from plants.models.user import User
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from plants.serializers.userSerializer import UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import plants.rolePermission as rolePermision

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve','destroy']:
            permission_classes = [permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
        
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData = {"email": request.data["email"],
                    "password": request.data["password"]}
        
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
    