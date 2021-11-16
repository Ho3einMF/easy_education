from django.urls import path

from user.views import SignupAPIView, ObtainAuthenticationToken, UserProfileAPIView

app_name = 'user'
urlpatterns = [
    path('token/', ObtainAuthenticationToken.as_view(), name='obtain-token'),
    path('signup/', SignupAPIView.as_view(), name='sign-up'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
]
