import secrets
from functools import wraps
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status



ACTIVE_TOKEN = None
test_iin = "123"
test_password = "123"

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = args[1].headers['Auth']
        if not token:
            return Response({"error": "Authentication token required"}, status=status.HTTP_401_UNAUTHORIZED) 
        
        if token != ACTIVE_TOKEN:
            return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)

        args[1].user = {
            "iin": test_iin, 
            "password": test_password
        }

        return func(*args, **kwargs)

    return wrapper

class TeacherLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        iin = request.data.get('iin')
        password = request.data.get('password')

        if not iin or not password:
            return Response({"error": "IIN and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        if iin == test_iin and password == test_password:
            global ACTIVE_TOKEN
            ACTIVE_TOKEN = secrets.token_urlsafe(32)
            return Response({
                "message": "Please change your password",
                "token": ACTIVE_TOKEN
            }, status=status.HTTP_200_OK)
        return Response({"error": "IIN or password entered incorrectly"}, status=status.HTTP_401_UNAUTHORIZED)


class ProtectedTeacherView(APIView):
    permission_classes = [AllowAny]

    @token_required
    def get(self, request):
        teacher = request.user
        return Response({
            "iin": teacher["iin"],
            "password": teacher["password"],
        }, status=status.HTTP_200_OK)
