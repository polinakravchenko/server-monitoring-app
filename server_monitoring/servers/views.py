from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from .models import Servers
from .forms import LoginForm
from .serializers import ServerSerializer

class ServerViewSet(viewsets.ModelViewSet):
    queryset = Servers.objects.all()
    serializer_class = ServerSerializer

    @action(detail=False, methods=['get'])
    def get_servers_by_localization(self, request):
        localization = request.query_params.get('localization')
        if not localization:
            return Response({"error": "Parameter 'localization' is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        servers = Servers.objects.filter(server_localization=localization)
        serializer = ServerSerializer(servers, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def server_details(self, request, pk=None):
        server = self.get_object()
        serializer = self.get_serializer(server)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def get_time(self, request):
        time_notification = Servers.objects.filter(time_notification=request.query_params.get('time_notification'))
        serializer = self.get_serializer(time_notification, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def upload_csv(self, request):
        if 'file' not in request.FILES:
            return Response({'error': 'No file was uploaded'}, status=400)

        csv_file = request.FILES['file']

        with open('media/' + csv_file.name, 'wb+') as destination:
            for chunk in csv_file.chunks():
                destination.write(chunk)
                
        return Response({'message': 'CSV file uploaded successfully'}, status=201)

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

def upload_form(request):
    return render(request, 'upload_form.html')
