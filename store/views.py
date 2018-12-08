from django.shortcuts import render,redirect
from store.forms import *
from store.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.core.files.storage import FileSystemStorage
def index(request):
	carros = Carro.objects.all()
	return render(request,'store/index.html',{'carros':carros})

def cadastro(request):
    form = UserModelForm(request.POST)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('/login')
    else:
    	form = UserModelForm()
    	return render(request, 'store/cadastro.html',{'form':form})

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

def add_car(request):
	if request.method == 'POST':
		form = CarroModelForm(request.POST, request.FILES)
		up_image = request.FILES['foto']
		fs = FileSystemStorage()
		name = fs.save(up_image.name, up_image)
		url = fs.url(name)
		marca = Marca.objects.get(id=request.POST['marca'])
		usuario = User.objects.get(id=request.POST['user'])
		carro = Carro(marca = marca, user = usuario, modelo = request.POST['modelo'], 
		ano_modelo = request.POST['ano_modelo'], ano_fabricacao = request.POST['ano_fabricacao'],
		nume_portas = request.POST['nume_portas'], foto = url)
		carro.save()
		return redirect('/add')
	else:
		form = CarroModelForm()
		return render(request, 'store/add_car.html', {'form':form})