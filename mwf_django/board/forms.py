from django import forms
from board.models import BulletinPost

class BulletinPostForm(forms.ModelForm):
	class Meta():
		model = BulletinPost
		fields = ('user', 'message')