from rest_framework import serializers
from .models import Tasks
from djoser.serializers import UserCreateSerializer
from rest_framework.response import Response
from .models import User

class UserRegistrationSerializer(UserCreateSerializer):
    date_joined = serializers.DateTimeField(format="%d-%m-%Y",read_only=True)
    class Meta(UserCreateSerializer.Meta):
        fields = ["id", "email", "username", "age","groups", "date_joined","password"]

#Serializerul din APIView
class TaskSerializer(serializers.ModelSerializer):
    username=serializers.StringRelatedField(source='user',read_only=True) #Creez o noua informatie adica in loc de user-pk afisez user-username
    user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),write_only=True)
    class Meta:
        model = Tasks
        fields = ["username","user","id","title","description","completed"]

#Serializer facut pt UserTaskSerializer
class TaskSerializer2(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),write_only=True)
    class Meta:
        model = Tasks
        fields = ["user","id","title","description","completed"]

class UserTaskSerializer(serializers.ModelSerializer):
    user_tasks = TaskSerializer2(source='tasks', many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "user_tasks"]

