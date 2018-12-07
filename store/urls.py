from django.urls import path, include
from . import views
urlpatterns = [
	path('',views.index,name='index'),
	path('cadastro/', views.cadastro, name='cadastro'),
	path('login/',views.do_login, name='login'),
 	path('logout/',views.do_logout, name='logout'),
 	path('perfil/',views.get_perfil, name='perfil'),
]