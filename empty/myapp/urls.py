from django.urls import path, include
from .views import UserCreateView, UserLoginView

urlpatterns = [
    path("", include("dj_rest_auth.urls")),  # 해당 라인 추가
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("signup/", UserCreateView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
]
