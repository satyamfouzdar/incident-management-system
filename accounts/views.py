from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import permissions


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def create_user(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save(password=serializer.validated_data['password'])
        return Response({'message': 'User created successfully', 'user_id': user.id}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)