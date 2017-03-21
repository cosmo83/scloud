from django.db import models
from django.contrib.auth.models import User
import uuid

class Organization(models.Model):
	org_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)	
	org_name = models.CharField(max_length=100)
	org_address = models.TextField()
	org_city = models.CharField(max_length=50)
	org_state = models.CharField(max_length=50)
	org_pin = models.CharField(max_length=6)
	org_taxno = models.CharField(max_length=50)

class UserProfile(models.Model):
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female')
	)	
	uid = uuid.uuid4()	
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	gender = models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
	avatar = models.ImageField(upload_to = 'static/avatars/'+str(uid), blank = True)
	date_of_birth = models.DateField(null=True)	
	
	def __str__(self):
        	return  self.user.username + " - " + self.user.first_name + " " + self.user.last_name

