from django.urls import path
from .views import UserRegistrationView, VerificationView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user-registration"),
    path("verify/", VerificationView.as_view(), name="verification"),
]
