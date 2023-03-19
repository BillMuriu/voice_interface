from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Matter
from .forms import MatterForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def create_matter(request):
    if request.method == 'POST':
        form = MatterForm(request.POST)
        if form.is_valid():
            matter = form.save()
            messages.success(request, 'Matter created successfully.')
            return redirect('matter_detail', matter_id=matter.id)
        else:
            messages.error(request, 'Invalid form data.')
    else:
        form = MatterForm()
    context = {'form': form}
    return render(request, 'create_matter.html', context)


def matter_detail(request, matter_id):
    matter = get_object_or_404(Matter, pk=matter_id)
    context = {'matter': matter}
    if request.method == 'POST':
        command = request.POST.get('command')
        if command == 'delete matter':
            matter.delete()
            messages.success(request, 'Matter deleted successfully.')
            return redirect('matters')
        else:
            messages.error(request, 'Invalid command.')
    return render(request, 'matter_detail.html', context)


def matters(request):
    matters = Matter.objects.all()
    context = {'matters': matters}
    return render(request, 'matters.html', context)

