from rest_framework import serializers
from client.models import ClientModel

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = "__all__"
