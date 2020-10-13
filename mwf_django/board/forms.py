from django import forms
from board.models import BulletinPost
from django.contrib.auth.models import User
from board.models import UserProfile


class BulletinPostForm(forms.ModelForm):
	class Meta():
		model = BulletinPost
		fields = ('user', 'message')


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	repeat_password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username', 'email', 'password')

	# this function will be used for the validation

	def clean(self):

		# data from the form is fetched using super function
		super(UserForm, self).clean()

		# extract the username and text field from the data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('repeat_password')

		# conditions to be met for the username length
		if password != password2:
			self._errors['password'] = self.error_class([
				'I\'m sorry, your passwords don\'t match.'])

		# return any errors if found
		return self.cleaned_data


class UserProfileForm(forms.ModelForm):
	class Meta():
		model = UserProfile
		fields = ('personal_site', 'profile_pic', 'birthday', 'bio', 'gender')
