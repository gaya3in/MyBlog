from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 50)
    img   = models.ImageField()
    date_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title