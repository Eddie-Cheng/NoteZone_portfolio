from django.db import models
from registration.models import Register
from django.db.models.signals import post_delete
from django.dispatch import receiver
from time import time

# Create your models here.
class Detail(models.Model):
    email = models.ForeignKey(Register)
    sentence = models.TextField(blank=True,null=True)
    https = models.URLField(blank=True,null=True)
    anyfile = models.FileField(upload_to='./upload/',blank=True,null=True)    
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text

#@receiver(post_delete, sender=Detail)
#def anyfile_post_delete_handler(sender, **kwargs):
#    Detail = kwargs['instance']
#    storage, path = Detail.anyfile.storage, Detail.anyfile.path
#    storage.delete(path)
    
