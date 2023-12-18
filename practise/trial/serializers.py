from rest_framework import serializers

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    roll_no = serializers.IntegerField()
    subject = serializers.CharField(max_length=50)