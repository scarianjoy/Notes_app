from django.shortcuts import render, redirect
from .models import List
from .forms import Listform
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = Listform(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all 
            messages.success(request, ('Notes have been added to the list'))
            return render(request, 'home.html', {'all_items': all_items})
    
    else:
            all_items = List.objects.all 
            return render(request, 'home.html', {'all_items': all_items})