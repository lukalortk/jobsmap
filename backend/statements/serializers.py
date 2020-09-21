from rest_framework import serializers
from .models import Job_Statement, Worker_Statement


class Job_Statement_Serializer(serializers.ModelSerializer):
    class Meta:
            model = Job_Statement
            fields = "__all__"


class Worker_Statement_Serializer(serializers.ModelSerializer):
    class Meta:
            model = Worker_Statement
            fields = "__all__"

