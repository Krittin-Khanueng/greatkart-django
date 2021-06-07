from django.urls import path
from . import views
urlpatterns = [
	path('register/', views.register, name='register'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('activate/<uidb64>/<token>/', views.activate, name="activate"),
	path('forgotPassword/', views.forgotPassword, name="forgotPassword"),
	path('restpassword_validate/<uidb64>/<token>/', views.restpassword_validate, name="restpassword_validate"),
	path('restPassword/', views.restPassword, name="restPassword"),
]