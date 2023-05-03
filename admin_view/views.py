import traceback
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import AdminProfile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from rest_framework.authtoken.models import Token
from client.models import ClientModel
from .serializer import AdminSerializer

@api_view(['post'])
@csrf_exempt
def login_admin(request):
    email = request.data['email']
    password = request.data['password']
    try:
        getUser = User.objects.get(username = email)
        user = authenticate(username=getUser, password=password)
        if user is not None:
            try:
                token = Token.objects.get(user = user)
                res = {'status': 200, 'token': token.key}
                return JsonResponse(res, status= 200, safe=False)
            except:
                traceback.print_exc()
                res = {"status": 500, "message": "Server error"}
                return JsonResponse(res, status=500, safe=False)
        else: 
            traceback.print_exc()
            res = {"status": 400, "message": "user not found"}
            return JsonResponse(res, status=400, safe=False)
    except:
        traceback.print_exc()
        res = {"status": 500, "message": "Enter all fields correctly"}
        return JsonResponse(res, status=500, safe=False)
   
    
@api_view(['Get'])
@csrf_exempt
def fetch_clients(request):
    if request.user.is_authenticated:
        try:
            getProduct = ClientModel.objects.all()
            serializer = AdminSerializer(getProduct, many= True)
            res = {"status": 200, "message": "successful", 'data': serializer.data}
            return JsonResponse(res, status=200, safe=False)
        except:
            traceback.print_exc()
            res = {"status": 500, "message": "Server error"}
            return JsonResponse(res, status=500, safe=False)
    else:
        traceback.print_exc()
        res = {"status": 400, "message": "user not authenticated"}
        return JsonResponse(res, status=400, safe=False)