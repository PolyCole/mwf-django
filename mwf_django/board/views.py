from django.shortcuts import render
from .models import BulletinPost
from .serializers import BulletinPostSerializer
from rest_framework import generics


# Create your views here.
class BulletinPostCreate(generics.ListCreateAPIView):
		queryset = BulletinPost.objects.all()
		serializer_class = BulletinPostSerializer 