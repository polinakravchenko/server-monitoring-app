from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from .models import Servers
from .forms import LoginForm

def servers(request):
  myservers = Servers.objects.all().values()
  template = loader.get_template('all_servers.html')
  context = {
    'myservers': myservers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  myserver = Servers.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myserver': myserver,
  }
  return HttpResponse(template.render(context, request))

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            return redirect('secure_page')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
  myservers = Servers.objects.all().values()
  template = loader.get_template('logout.html')
  context = {
    'myservers': myservers,
  }
  return HttpResponse(template.render(context, request))

@login_required
def secure_page(request):
    user_name = request.user.username
    return render(request, 'secure.html', {'user_name': user_name})