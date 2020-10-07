from django.contrib import admin
from board.models import BulletinPost
from board.models import UserProfile

# Register your models here.
admin.site.register(BulletinPost)
admin.site.register(UserProfile)