from django.db import models
from django.utils import timezone

# Create your models here.
class client(models.Model):
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class meeting(models.Model):
	sessionid = models.CharField(max_length=10)
	user_name = models.CharField(max_length=50)
	audio = models.FileField(upload_to='uploads/')
	script = models.FileField(upload_to='uploads/')
	dateTime = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.sessionid


	