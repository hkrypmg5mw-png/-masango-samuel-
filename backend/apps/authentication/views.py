import secrets
import string
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, UserSerializer, MyTokenObtainPairSerializer, ChangePasswordSerializer
from .permissions import IsAdminUser
from django.contrib.auth import get_user_model
from services.twilio_service import TwilioService

User = get_user_model()

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

class CreateStaffView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        data = request.data
        role = data.get('role')
        if role not in ['NURSE', 'DOCTOR', 'CHW', 'ADMIN']:
            return Response({"error": "Invalid role"}, status=status.HTTP_400_BAD_REQUEST)

        # Generate temporary password
        alphabet = string.ascii_letters + string.digits
        temp_password = ''.join(secrets.choice(alphabet) for i in range(12))

        user = User.objects.create_user(
            email=data.get('email'),
            password=temp_password,
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            role=role,
            must_change_password=True
        )

        return Response({
            "message": "Staff account created",
            "email": user.email,
            "temporary_password": temp_password
        }, status=status.HTTP_201_CREATED)

class VerifyOTPView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        twilio = TwilioService()
        if twilio.check_verification_code(phone_number, code):
            user = User.objects.filter(phone_number=phone_number).first()
            if user:
                user.is_verified = True
                user.save()
            return Response({"message": "Verification successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid code"}, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        if not user.check_password(serializer.data.get("old_password")):
            return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(serializer.data.get("new_password"))
        user.must_change_password = False
        user.save()
        return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
