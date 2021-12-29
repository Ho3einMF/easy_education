from django.urls import path

from user.views import SignupAPIView, ObtainAuthenticationToken, UserProfileAPIView, ChangePasswordAPIView, \
    TeacherCreateAPIView

app_name = 'user'
urlpatterns = [
    path('token/', ObtainAuthenticationToken.as_view(), name='obtain-token'),
    path('signup/', SignupAPIView.as_view(), name='sign-up'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
    path('teacher/', TeacherCreateAPIView.as_view(), name='teacher-create'),
    path('profile/change_password/', ChangePasswordAPIView.as_view(), name='change-password'),
]
