from rest_framework import serializers
from users.models import *

class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"

class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"

class StudentsAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentsAddress
        fields = "__all__"        
class StudentsDetailsAddressSerializers(serializers.ModelSerializer):
    address = StudentsAddressSerializers()
    class Meta:
        model = Students
        fields = ('first_name','surname','mobile_number','Birth','address')