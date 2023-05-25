from django.contrib.auth.models import User
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
import random

from .serializers import UserSerializer, VerificationSerializer


class UserRegistrationView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            id = serializer.validated_data["id"]
            email = serializer.validated_data["email"]

            # Generate verification code
            verification_code = str(random.randint(100000, 999999))

            # Save verification code to the user's profile or database

            # Send verification code via email
            subject = "Verification Code"
            message = f"Your verification code is: {verification_code}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)

            return Response({"message": "Verification code sent successfully."})
        else:
            return Response(serializer.errors, status=400)


class VerificationView(APIView):
    serializer_class = VerificationSerializer

    def post(self, request):
        serializer = VerificationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            verification_code = serializer.validated_data["verification_code"]

            # Retrieve the user by email
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return Response({"message": "User not found."}, status=400)

            # Compare the verification code
            stored_verification_code = (
                user.profile.verification_code
            )  # Assuming verification_code is a field in the user's profile
            if verification_code == stored_verification_code:
                # Verification successful
                # Perform additional actions (e.g., activate the account, update the user's status, etc.)
                return Response({"message": "Verification successful."})
            else:
                # Verification failed
                return Response({"message": "Invalid verification code."}, status=400)
        else:
            return Response(serializer.errors, status=400)
