from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length= 200)
    content = models.CharField(max_length= 200)
    price = models.IntegerField(default= 0)
    # created_at = models.DateTimeField(auto_now_add=True)


