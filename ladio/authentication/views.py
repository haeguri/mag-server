from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLogin
from rest_framework import viewsets, permissions, status, views
from rest_framework.response import Response

from django.contrib.auth import get_user_model, authenticate, login, logout

from .serializers import UserSerializer
from .permissions import IsUserOwner

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # 위험하지 않은 HTTP method('GET', 'HEAD', 'OPTION')는 모두 허용한다.
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
        # 회원가입은 POST 요청으로 이뤄지므로 허용한다.
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsUserOwner(),)

    def create(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            User.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status':'Bad request',
            'message': 'User could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    def post(self, request, format=None):
        user = authenticate(email=request.data['email'], password=request.data['password'])

        if user is not None:
            if user.is_active:
                login(request, user)

                serialized = UserSerializer(user)

                return Response(serialized.data)
            else:
                return Response({
                    'status':'Unauthorized',
                    'message':'This user has been disabled'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status':'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format = None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)


class FacebookLogin(SocialLogin):
    adapter_class = FacebookOAuth2Adapter
