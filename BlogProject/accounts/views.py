from rest_framework.generics import CreateAPIView
from .serializers import Registerserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class StudentRegister(APIView):

    def post(self,request):
        try:
            data = request.data
            serializer = Registerserializer(data=data)

            if serializer.is_valid():
                serializer.save()       #this is used to save data
                response_data={'data':serializer.data,'message':'User Registerd successfully'}
                return Response(response_data,status = status.HTTP_201_CREATED)
            
            else:
                response_data={'data':serializer.errors}
                return Response(response_data,status = status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({'data':serializer.errors},status = status.HTTP_400_BAD_REQUEST)

              