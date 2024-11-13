from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    phone_number=serializers.IntegerField()