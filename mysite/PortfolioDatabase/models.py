from django.db import models

# Create your models here.
class portfolio(models.Model):
    def __str__(self):
        a= self.port_name + self.port_desc
        return a
    port_name = models.CharField(max_length=200)
    port_desc = models.CharField(max_length=200)

class hobbies(models.Model):
    def __str__(self):
        return self.hob_name + self.hob_desc
    hob_name = models.CharField(max_length=200)
    hob_desc = models.CharField(max_length= 200)