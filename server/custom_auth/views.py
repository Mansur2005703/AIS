import hashlib
import random
import string
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

TOKEN = ""

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    # Получаем логин и пароль из запроса
    login = request.data.get('login')
    password = request.data.get('password')

    # Хэшируем введённый пароль
    TOKEN = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

    
    if login and password:
        data = {'status': "success", 'token': TOKEN}
        return Response(data, status=200)
    else:
        data = {'status': "error", 'message': "Invalid login or password"}
        return Response(data, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def auth(request):
    token = request.data.get('token')
    
    data = {"iin": "12344233242"}
    
    if TOKEN == token:
        mess = {'status': "error", 'message': "Forribiden"}
        return Response(mess, status=403)
    
    data = {'status': "success", 'data': data}
    return Response(data, status=200)