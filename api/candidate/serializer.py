from rest_framework import serializers
from .models import StudentModel
class StudentSer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'   # to display all fields from
