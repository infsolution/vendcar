from django.shortcuts import render,redirect
from store.forms import *
from store.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
def index(request):
	return render(request,'store/index.html')

def cadastro(request):
    form = UserModelForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'store/cadastro.html', context)

def do_login(request):
	if request.method == 'POST':
		user = authenticate(username = request.POST['username'], password =  request.POST['password'])
		if user is not None:
			login(request,user)
			return redirect('/', user)
	return render(request, 'store/login.html')

def do_logout(request):
	logout(request)
	return redirect('/login')

@login_required
def get_perfil(request):
	return render(request, 'store/perfil.html')