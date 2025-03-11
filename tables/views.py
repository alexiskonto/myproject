from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TableEntry

@login_required
def dashboard(request):
    table_entries = TableEntry.objects.filter(user=request.user)
    return render(request, 'tables/dashboard.html', {'table_entries': table_entries})

@login_required
def add_entry(request):
    if request.method == "POST":
        name = request.POST['name']
        value = request.POST['value']
        TableEntry.objects.create(user=request.user, name=name, value=value)
        return redirect('dashboard')
