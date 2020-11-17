from django.shortcuts import render
from board.forms import BulletinPostForm
from django.http import HttpResponseRedirect
from board.forms import UserForm
from board.forms import UserProfileForm
from django.http import HttpResponseRedirect,HttpResponse


# Create your views here.
def index(request):
    cont = {}

    if request.method == "POST":
        bulletin_form = BulletinPostForm(data=request.POST)

        if bulletin_form.is_valid():
            bulletin_post = bulletin_form.save()
            print(bulletin_post.message)
            return render(request, 'frontend/index.html', cont)
        else:
            print(bulletin_form.errors)

    else:
        cont['bulletin_form'] = BulletinPostForm()

    cont['authenticated'] = request.user.is_authenticated

    print("Returning from index in frontend/views.py")
    return render(request, 'frontend/index.html', cont)

def register(request):
    context = {}
    Registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            Registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()


    context['user_form'] = user_form
    context['profile_form'] = profile_form
    context['registered'] = Registered
    return render(request, 'frontend/register.html', context)
