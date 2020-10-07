from django.shortcuts import render
from board.forms import BulletinPostForm
from django.http import HttpResponseRedirect
from board.forms import UserForm
from board.forms import UserProfileForm


# Create your views here.
def index(request):
    cont = {}

    if request.method == "POST":
        bulletin_form = BulletinPostForm(data=request.POST)

        if bulletin_form.is_valid():
            bulletin_post = bulletin_form.save()
        else:
            print(bulletin_form.errors)

    else:
        cont['bulletin_form'] = BulletinPostForm()

    cont['authenticated'] = request.user.is_authenticated


    return render(request, 'frontend/index.html', cont)

def register(request):
    context = {}
    context['user_form'] = UserForm()
    context['profile_form'] = UserProfileForm()
    return render(request, 'frontend/register.html', context)