from django.db import models

# Create your models here.


class BulletinPost(models.Model):
	user = models.CharField(max_length=127, default="anonymous")
	message = models.TextField(max_length=5000)
	created_at = models.DateTimeField(auto_now_add=True)