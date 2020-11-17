from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import datetime


# Create your models here.

class UserProfile(models.Model):

	# Our foreign key to an existing user.
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	class Genders(models.TextChoices):
		MALE = 'M', _('Male')
		FEMALE = 'F', _('Female')
		OTHER = 'O', _('Other')

	# Gender
	gender = models.CharField(
		max_length=2,
		choices=Genders.choices,
		default=Genders.OTHER,
	)

	# Birthdate
	birthday = models.DateField(auto_now=False, auto_now_add=False, blank=False, default=datetime.date.today)

	# Slug field (profile bio)
	bio = models.CharField(max_length=127, blank=True)

	personal_site = models.URLField(blank=True)

	profile_pic = models.ImageField(upload_to='profile-pictures', blank=True)

	def __str__(self):
		return self.user.username


class BulletinPost(models.Model):
	user = models.CharField(max_length=127, default="anonymous")
	message = models.TextField(max_length=5000)
	created_at = models.DateTimeField(auto_now_add=True)
