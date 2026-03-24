from django.shortcuts import render
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from .models import Tasks,User
from rest_framework import filters
from .serializers import TaskSerializer,UserTaskSerializer
# Create your views here.

class TaskView(generics.ListCreateAPIView):
    serializer_class=TaskSerializer
    permission_classes=[IsAuthenticated]
    queryset=Tasks.objects.all()
    filter_backends=[filters.SearchFilter,filters.OrderingFilter]
    search_fields=["id","user__username","title","completed","description"] # user__username Din Relatia cu User aleg fieldul de username
#Reconfigurez metoda de POST sa accepte o lista de obiecte JSON
    def create(self,request,*args,**kwargs):
         is_many=isinstance(request.data,list)
         model_objects=self.get_serializer(data=request.data,many=is_many) #data=request.data pentru ca fac deserializare
         model_objects.is_valid(raise_exception=True)
         model_objects.save()
         return Response(model_objects.data, status=201)


class SingleTaskView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=TaskSerializer
    permission_classes=[IsAuthenticated]
    queryset=Tasks.objects.all()


class UserTaskView(generics.RetrieveAPIView):
    serializer_class=UserTaskSerializer
    permission_classes=[IsAuthenticated]
    queryset=User.objects.all()