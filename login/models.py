from django.db import models

# Create your models here.
class Attachments(models.Model):
    profile_image_url = models.FileField(upload_to='upload/')
    entity_id         = models.IntegerField(max_length=11)
    entity_code       = models.CharField(max_length=100)
    is_deleted        = models.IntegerField(max_length=11)


