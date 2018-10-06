from django.db import models
from django.utils import timezone

# Create your models here.
class client(models.Model):
	email = models.CharField(primary_key = True, max_length=50, default='null')
	nickName = models.CharField(max_length=20, default='null')
	password = models.CharField(max_length=20)

	def __str__(self):
		return self.email

class meeting(models.Model):
	sessionid = models.CharField(primary_key = True, max_length=50)
	name = models.CharField(max_length=50, null=True)
	user_name = models.CharField(max_length=500, null=True)
	script = models.CharField(max_length=5000000000, null=True)
	dateTime = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name