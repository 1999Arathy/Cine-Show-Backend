from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_201_CREATED
)
from rest_framework.response import Response
from .serializers import RegisterSerializer, MovieSerializer, BookingSerializer,TicketSerializer
from django.http import JsonResponse, HttpResponse
from .models import Movie, usermodel
from rest_framework.authentication import TokenAuthentication
# import qrcode
# import base64
# import io
# from PIL import Image;
# from qrcode.image.pil import PilImage


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def Login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error' : 'please enter both'}, status = HTTP_400_BAD_REQUEST)
    user = authenticate(username = username, password = password)
    if not user:
        return Response({'error' : 'Invalid user'}, status = HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user = user)
    return Response({'token' : token.key}, status = HTTP_200_OK)


@api_view(['POST'])
@permission_classes((AllowAny,))
def Registration(request):
    if request.method =='POST':
        # return Response(request.data)
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= HTTP_201_CREATED) 
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def Logout(request):
    if request.method =='POST':
        try :
            request.user.auth_token.delete()
            return Response({'success':'user logged out successfully'}, status = HTTP_200_OK)

        except Exception as e:
            return Response({'error':'str(e)'}, status = HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['GET'])
def MovieList(request):
    if request.method == 'GET':
        mydata = Movie.objects.all()
        serialized_data = MovieSerializer(mydata, many=True)
        return JsonResponse(serialized_data.data, safe = False)



@csrf_exempt
@api_view(['GET'])
def DetailView(request,id):
    
    try:
        mydata = Movie.objects.get(id=id)

    except Movie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET': 
        serializer = MovieSerializer(mydata)
        return JsonResponse(serializer.data)

@csrf_exempt
@api_view(['GET'])
def Ticket(request,user):
    qr_code_image = None
    if request.method == 'GET':
        mydata = usermodel.objects.filter(User_name = user).values()
        serialized_data = TicketSerializer(mydata, many=True)

        # qr = qrcode.QRCode(
        #         version=1,
        #         error_correction=qrcode.constants.ERROR_CORRECT_L,
        #         box_size=10,
        #         border=4,
        #     )
        # qr.add_data(serialized_data)
        # qr.make(fit=True)

        # qr_code_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        #     # Create a BytesIO buffer to temporarily store the image
        # buffer = io.BytesIO()
        # qr_code_image.save(buffer, format="PNG")
        # qr_code_image_data = base64.b64encode(buffer.getvalue()).decode()


        return JsonResponse(serialized_data.data, safe = False)
        

@csrf_exempt
@api_view(['POST'])
def Booking(request):
    if request.method == 'POST':
        serializer = BookingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= HTTP_201_CREATED) 
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



