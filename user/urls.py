from django.urls import path

from user.views import SignupAPIView, ObtainAuthenticationToken

app_name = 'user'
urlpatterns = [
    path('token/', ObtainAuthenticationToken.as_view()),
    path('signup/', SignupAPIView.as_view(), name='sign-up'),
]
