from django.db import models

# Create your models here.
class portfolio(models.Model):
    def __str__(self):
        a= self.port_name
        return a
    port_id = models.IntegerField()
    port_name = models.CharField(max_length=200)
    port_desc = models.CharField(max_length=200)
    port_imag = models.CharField(max_length=500, default='https://www.library.yorku.ca/ds/wp-content/uploads/2021/07/digitalportfolio.png')

class hobbies(models.Model):
    def __str__(self):
        return self.hob_name
    hob_id = models.IntegerField()
    hob_name = models.CharField(max_length=200)
    hob_desc = models.CharField(max_length= 200)
    hob_imag = models.CharField(max_length= 500, default='https://www.shutterstock.com/image-vector/hobby-concept-music-video-game-260nw-1451106167.jpg')