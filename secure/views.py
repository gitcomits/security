from django.shortcuts import render
from .models import Info
from .forms import InfoForm
from django.contrib import messages
# Create your views here.

def home(request):
    all_db = Info.objects.all
    if request.method == 'POST':
        form = InfoForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Thank you for your info'))
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            age = request.POST['age']
            messages.success(request, ('Info not valid'))
            return render(request, 'home.html', {'all':all_db})

    return render(request, 'home.html', {'all':all_db})




