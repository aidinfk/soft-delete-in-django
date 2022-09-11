from django.db import models
from django.db.models import Manager
from soft.models import Soft

# Create your models here.
class Person(Soft):
    title = models.CharField(max_length=255)


    class Meta:
        default_manager_name = 'objects'

class RecyclePerson(Person):
    deleted = Manager()
    class Meta:
        proxy = True