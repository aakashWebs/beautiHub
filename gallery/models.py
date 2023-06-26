from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.CharField(max_length=1000)
    added_by    = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='added_by',default=None)
    added_date  = models.DateTimeField(auto_now_add=True)
    updated_by  = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='updated_by',default=1)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.name)