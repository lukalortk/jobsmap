from django.db import models

class Job_Statement(models.Model):
    job_title = models.CharField(max_length=50)
    job_description = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    job_area = models.CharField(max_length=50)
    uid = models.CharField(max_length=100)
    image = models.CharField(max_length=400)


    def __str__(self):
        return self.job_title


class Worker_Statement(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    job_area = models.CharField(max_length=50)
    uid = models.CharField(max_length=100)
    image = models.CharField(max_length=400)


    def __str__(self):
        return self.name
