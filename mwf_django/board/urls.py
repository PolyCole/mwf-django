from django.urls import path
from . import views

urlpatterns = [
	path('api/bulletinpost/', views.BulletinPostCreate.as_view()),
]