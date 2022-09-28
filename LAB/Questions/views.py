from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login_user/')
def profile(request):
    return render(request, 'profile.html')


def index_view(request):
	context = {'name': ''}
	if request.user is not None:
		context['name'] = request.user.get_username
	return render(request, 'index.html', context)