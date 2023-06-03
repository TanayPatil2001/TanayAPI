from django.shortcuts import render
from .models import StudentModel
from .serializer import StudentSer

from  rest_framework .views import APIView
from rest_framework .response import Response
from rest_framework import status

# Creating Class for GET & POST methods
class StudentViewgetpost(APIView):
    # Function for GET method
    def get(self,r):
        obj = StudentModel.objects.all()
        ser = StudentSer(obj, many=True)
        return Response(ser.data)

    # Function for POST method
    def post(self, r):
        obj = StudentView(data=r.data)
        if obj.is_valid():
            obj.save()
            return Response(obj.data, status=status.HTTP_201_CREATED)
        return Response(obj.errors, status=status.HTTP_400_BAD_REQUEST)

# Creating Class for UPDATE & DELETE methods
class StudentViewupdatedelete(APIView):
    # Function for DELETE method
    def delete(self,r,ab):
        obj = StudentModel.objects.get()
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Function for PUT method
    def put(self,r,ab):
        obj = StudentModel.objects.get(ab=ab)
        serobj = StudentSer(obj,data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)