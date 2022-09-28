from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		print('test')
		if user is not None:
			login(request, user)
			return redirect('Home')
		else:
			print('1')
			messages.success(request, 'There was an error logging you in, please try again.')
			return redirect('Login')
			print('2')

	else:
		return render(request, 'login.html', {})



@login_required(login_url='/login_user/')
def logout_view(request):
	logout(request)
	messages.success(request, 'You have been logged out.')
	return redirect('Home')


def register_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('Home')
		else:
			messages.success(request, 'Something went wrong, please try again.')
			return redirect('Register')
	else:
		return render(request, 'register.html', {'form': UserCreationForm()})