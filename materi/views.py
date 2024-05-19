from django.shortcuts import render, redirect
from .models import Materi
from .forms import MateriForm

def materi_list(request):
    materials = Materi.objects.all()
    return render(request, 'materi_list.html', {'materials': materials})

def upload_materi(request):
    if request.method == 'POST':
        form = MateriForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('materi_list')
    else:
        form = MateriForm()
    return render(request, 'upload_materi.html', {'form': form})
