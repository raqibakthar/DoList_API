from rest_framework import serializers
from .models import TodoModel

class TodoSerializer(serializers.ModelSerializer):

    class Meta:

        model = TodoModel
        exclude = ['created_at','updated_at']
