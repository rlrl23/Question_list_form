import datetime
from django.db import models

# Create your models here.

class Division(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200)
    division_id=models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = "companies"

class Questions(models.Model):
    date_time=models.DateTimeField(default=datetime.datetime.now())
    division_id=models.ForeignKey(Division, on_delete=models.PROTECT)
    company=models.ForeignKey(Company, on_delete=models.PROTECT)
    no_name_company=models.CharField(max_length=200, null=True, blank=True)
    question=models.TextField()
    email=models.EmailField(null=True, blank=True)

    def __str__(self):
        return f'Question №{self.pk}'

    class Meta():
        verbose_name_plural = "questions"