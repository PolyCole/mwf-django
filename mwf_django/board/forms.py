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

	def clean_new_password2(self):
            password1 = self.cleaned_data.get('password')
            password2 = self.cleaned_data.get('repeat_password')
            if password1 and password2:
                if password1 != password2:
                    raise forms.ValidationError(
                        self.error_messages['password_mismatch'],
                        code='password_mismatch',
                    )
              # I think this line is checking whether the user's password matches their
              # previous password.
#             password_validation.validate_password(password2, self.user)
            return password2


class UserProfileForm(forms.ModelForm):
	class Meta():
		model = UserProfile
		fields = ('portfolio_site', 'profile_pic')
