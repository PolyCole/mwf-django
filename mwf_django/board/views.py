from django.shortcuts import render
from .models import BulletinPost
from .serializers import BulletinPostSerializer
from rest_framework import generics
import datetime
from pytz import timezone

def fix_date(obj):
    obj.created_at = obj.created_at.replace(tzinfo=timezone('US/Mountain')).strftime("%B %d, %Y at %H:%M %p")
    return obj

# Create your views here.
class BulletinPostCreate(generics.ListCreateAPIView):
    queryset = BulletinPost.objects.all().order_by('-created_at')
    queryset = map(fix_date, queryset)

    serializer_class = BulletinPostSerializer
