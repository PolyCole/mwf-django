from django.urls import path
from . import views

urlpatterns = [
	path('api/bulletinpost/', views.BulletinPostCreate.as_view()),
	path('user_login/', views.user_login, name='user_login'),
	path('logout/', views.user_logout, name="logout")
]