# Create your views here.
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.conf import USER_CREATION_MESSAGE
from user.serializers import SignupUserSerializer, TokenSerializer, TeacherSerializer


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
        return Response(TeacherSerializer(request.user).data, status=status.HTTP_200_OK)
