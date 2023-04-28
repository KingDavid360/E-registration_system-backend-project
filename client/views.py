import traceback
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import ClientModel

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
    phone_number=request.data["phone_number"]
    birthday=request.data["birthday"]
    institution=request.data["institution"]
    type_of_institution=request.data["type_of_institution"]
    address=request.data["address"]
    city=request.data["city"]
    state=request.data["state"]
    course=request.data["course"]
    grade_level=request.data["grade_level"]

    try:
        client=ClientModel.objects.create(
            staff_id=staff_id,
            nin=nin,
            email=email,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            gender=gender,
            phone_number=phone_number,
            birthday=birthday,
            institution=institution,
            type_of_institution=type_of_institution,
            address=address,
            city=city,
            state=state,
            course=course,
            grade_level=grade_level,
        )
        client.save()
        res = {'status': 200, 'message': "Successful"}
        return JsonResponse(res, status= 200, safe= False)
    except:
        traceback.print_exc()
        res = {"status": 500, "message": "Enter all fields correctly"}
        return JsonResponse(res, status=500, safe=False)

