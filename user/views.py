# Create your views here.
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.conf import USER_CREATION_MESSAGE, PASSWORD_CHANGED_MESSAGE
from user.serializers import SignupUserSerializer, TokenSerializer, UserProfileSerializer, ChangePasswordSerializer
from user.utils import get_user_or_404


class SignupAPIView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = SignupUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'details': USER_CREATION_MESSAGE}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObtainAuthenticationToken(ObtainAuthToken):
    serializer_class = TokenSerializer


class UserProfileAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserProfileSerializer(request.user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update Profile
    def put(self, request):
        instance = get_user_or_404(user_id=request.user.id)
        serializer = UserProfileSerializer(instance=instance, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def patch(self, request):
        instance = get_user_or_404(user_id=request.user.id)
        serializer = ChangePasswordSerializer(instance=instance, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'details': PASSWORD_CHANGED_MESSAGE}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
