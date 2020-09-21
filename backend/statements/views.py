from .models import Job_Statement, Worker_Statement
from .serializers import Job_Statement_Serializer, Worker_Statement_Serializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class Job_Statement_View_Set(viewsets.ModelViewSet):
    queryset = Job_Statement.objects.all()
    serializer_class = Job_Statement_Serializer 
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("job_area","category")


class Worker_Statement_View_Set(viewsets.ModelViewSet):
    queryset = Worker_Statement.objects.all()
    serializer_class = Worker_Statement_Serializer   




