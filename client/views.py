from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

@api_view(['post'])
@csrf_exempt
def register_user(request):
    staff_id=request.data["staff_id"]
    nin=request.data["nin"]
    email=request.data['email']
    first_name=request.data["first_name"]
    last_name=request.data["last_name"]
    middle_name=request.data["middle_name"]
    gender=request.data["gender"]
    birthday=request.data["birthday"]
    institution=request.data["institution"]
    type_of_institution=request.data["type_of_institution"]
    address=request.data["address"]
    city=request.data["city"]
    state=request.data["state"]
    course=request.data["course"]

