from django.shortcuts import render
from board.forms import BulletinPostForm

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

	
	return render(request, 'frontend/index.html', cont)