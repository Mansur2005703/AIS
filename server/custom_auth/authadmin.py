import os
import secrets
from functools import wraps
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from dotenv import load_dotenv

load_dotenv()

# HASH_PASSWORD1 = os.getenv('HASH_PASSWORD1')
# HASH_PASSWORD2 = os.getenv('HASH_PASSWORD2')
HASH_PASSWORD1= 'TWUFpOACWoBA'
HASH_PASSWORD2= 'fLHWeoFIeShf'

ACTIVE_TOKEN = None

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = args[1].headers.get('Auth')
        if not token:
            return Response({"error": "Authentication token required"}, status=status.HTTP_401_UNAUTHORIZED)

        if token != ACTIVE_TOKEN:
            return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)

        return func(*args, **kwargs)

    return wrapper

class AdminLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        hash1 = request.data.get('hash1')
        hash2 = request.data.get('hash2')  
        if not hash1 or not hash2:
            return Response({"error": "Not all hashes have been transmitted"}, status=status.HTTP_400_BAD_REQUEST)
        if hash1 == HASH_PASSWORD1 and hash2 == HASH_PASSWORD2:
            global ACTIVE_TOKEN 
            ACTIVE_TOKEN = secrets.token_urlsafe(32)
            return Response({
                "message": "Login successful",
                "token": ACTIVE_TOKEN
            }, status=status.HTTP_200_OK)

        return Response({"error": "Invalid hash"}, status=status.HTTP_401_UNAUTHORIZED)


class ProtectedAdminView(APIView):
    permission_classes = [AllowAny]

    @token_required
    def get(self, request):
        return Response({
            "message": "Admin is authenticated"
        }, status=status.HTTP_200_OK)
