from django.urls import path

from user.views import SignupAPIView

app_name = 'user'
urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='sign-up'),
]
