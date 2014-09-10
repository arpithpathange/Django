from django.db import models

class Registration(models.Model):
	phoneno = models.IntegerField(default=0)
	email = models.CharField(max_length=200)




