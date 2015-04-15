from django.db import models

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    website = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    email = models.EmailField(verbose_name='e-mail')
    password = models.CharField(max_length=20)

    def __unicode__(self):
        return self.username


