from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, Http404
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.contrib import messages
from .serializers import CamDBSerializer
from .forms import UserRegistrationForm
from .forms import CamDBForm
from .models import CamDB

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    camdb = CamDB.objects.all()    
    return render(request, 'home.html', {'camdb': camdb})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def add_camdb(request):
    if request.method == 'POST':
        form = CamDBForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Объявление успешно добавлено!')
            return redirect('camdb_list')
    else:
        form = CamDBForm()
    return render(request, 'add_camdb.html', {'form': form})

def camdb_list(request):
    camdb = CamDB.objects.all()
    return render(request, 'camdb_list.html', {'camdb': camdb})

def user_logout(request):
    logout(request)
    return redirect('login')

def delete_all_ads(request):
    if request.method == 'POST':
        CamDB.objects.all().delete()  
        return redirect('home') 
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

class CamDBDetailView(generics.RetrieveAPIView):
    queryset = CamDB.objects.all()
    serializer_class = CamDBSerializer

def camdb_detail(request, camdb_id):
    # Поиск объекта по уникальному camdb_id
    ad = get_object_or_404(CamDB, camdb_id=camdb_id)
    data = {
        'title': ad.title,
        'camdb_id': ad.camdb_id,
        'author': ad.author,
        'views': ad.views,
        'position': ad.position,
    }
    return JsonResponse(data)

def view_camdb_json(request, camdb_id):
    if camdb_id:
        try:
            camdb = CamDB.objects.get(camdb_id=camdb_id)
            data = {
                'camdb_id': camdb.camdb_id,
                'title': camdb.title,
                'author': camdb.author,
                'views': camdb.views,
                'position': camdb.position,
            }
            return JsonResponse(data)
        except CamDB.DoesNotExist:
            return JsonResponse({'error': 'Объявление не найдено'}, status=404)
    else:
        return JsonResponse({'error': 'ID не указан'}, status=400)