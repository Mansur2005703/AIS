# from django.contrib.auth import authenticate
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework import status
# from .models import Teacher

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.tokens import RefreshToken

# from .models import Teacher  # Убедись, что у тебя есть эта модель

# class TeacherLoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         # Жестко заданные данные
#         hardcoded_iin = '0503'
#         hardcoded_password = '0503'

#         # Получаем данные из запроса
#         iin = request.data.get('iin')
#         password = request.data.get('password')

#         # Проверка на наличие ИИН и пароля
#         if not iin or not password:
#             return Response({"error": "IIN and password are required"}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             # Проверяем ИИН и пароль с жестко заданными значениями
#             if iin == hardcoded_iin and password == hardcoded_password:
#                 # Создаем фейковый объект Teacher (имитация пользователя)
#                 user = Teacher(iin=iin, password=password)
#                 user.id = 1  # Устанавливаем id вручную для теста

#                 # Генерация токена для фейкового пользователя
#                 refresh = RefreshToken.for_user(user)
#                 return Response({"token": str(refresh.access_token)}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"error": "IIN or password entered incorrectly"}, status=status.HTTP_401_UNAUTHORIZED)

#         except Exception as e:
#             # Обработка внутренних ошибок сервера
#             print(f"Error: {e}")  # Логирование ошибки для отладки
#             return Response({"error": "Server error, please try again later"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

import secrets
from functools import wraps
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status


def token_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        token = request.headers.get("Auth")

        print(f"Authorization Header: {token}")
        if not token:
            return Response({"error": "Authentication token required"}, status=status.HTTP_401_UNAUTHORIZED)

        valid_tokens = ["testtoken12345"]  
        if token not in valid_tokens:
            return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)

        request.user = {
            "iin": "0503", 
            "password": "0503"
        }

        return func(request, *args, **kwargs)

    return wrapper

class TeacherLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        iin = request.data.get('iin')
        password = request.data.get('password')

        if not iin or not password:
            return Response({"error": "IIN and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Тестовые данные
        test_iin = "0503"
        test_password = "0503"

        if iin == test_iin and password == test_password:
            token = secrets.token_urlsafe(32)
            return Response({
                "message": "Please change your password",
                "token": token
            }, status=status.HTTP_200_OK)

        if iin == test_iin and password != test_password:
            token = secrets.token_urlsafe(32)
            return Response({
                "message": "Password changed successfully",
                "token": token
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
