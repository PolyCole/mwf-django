from django.shortcuts import render
from .models import BulletinPost
from .serializers import BulletinPostSerializer
from rest_framework import generics
import datetime
from pytz import timezone
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def fix_date(obj):
    obj.created_at = obj.created_at.strftime("%B %d, %Y at %H:%M %p")
    return obj


# Create your views here.
class BulletinPostCreate(generics.ListCreateAPIView):
    print("BulletinPostCreate in board/views.py")
    queryset = BulletinPost.objects.all().order_by('-created_at')
    queryset = map(fix_date, queryset)

    serializer_class = BulletinPostSerializer


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Account not active.")
        else:
            print("User failed to authenticate.")
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'frontend/login.html', {})


# SOMETIMES people fragment all the views into separate folders or things,
# and then use this file to aggregate. Would be helpful in larger projects.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
