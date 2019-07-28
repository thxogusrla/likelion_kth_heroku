from django.db import models

# Create your models here.
class Portoflio(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField() #images/ 폴더에다가 업로드 해줄 거다.
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title