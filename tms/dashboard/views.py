from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'index.html')

def users(request):
    return render(request, 'users.html')

