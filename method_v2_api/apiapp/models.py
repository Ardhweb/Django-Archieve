from django.db import models

# Create your models here.
from django.db import models

class APIMODEL(models.Model):
	name = models.CharField(max_length=50)
