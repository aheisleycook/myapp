from django.db import models
from django.utils import timezone
# Create your models here.
class Entry(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(help_text="this is mandatory",max_length=12)
    description = models.TextField()
    posted_at = models.DateTimeField()
    def Get_Post(self) -> object:
        return timezone.now()
    def __str__(self):
        return self.title + " " + self.description + "" + self.Get_Post()

class User(models.Model):
    username = models.CharField(primary_key=True, max_length=23,unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=23)
    postby =  models.ForeignKey("Entry",on_delete=models.CASCADE)



