from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

	# Our foreign key to an existing user.
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	# User doesn't have to fill it out.
	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to='profile-pictures', blank=True)

	def __str__(self):
		return self.user.username


class BulletinPost(models.Model):
	user = models.CharField(max_length=127, default="anonymous")
	message = models.TextField(max_length=5000)
	created_at = models.DateTimeField(auto_now_add=True)
