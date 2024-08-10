from django.shortcuts import render, redirect, get_object_or_404
from .models import Entry
from .forms import EntryForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

def index(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EntryForm()
    entries = Entry.objects.all()
    return render(request, 'journal/index.html', {'form': form, 'entries': entries})

def edit_entry(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EntryForm(instance=entry)
    return render(request, 'journal/edit_entry.html', {'form': form})

def delete_entry(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if not request.user.is_superuser:
        return redirect('index')
    if request.method == 'POST':
        entry.delete()
        return redirect('index')
    return render(request, 'journal/delete_entry.html', {'entry': entry})

def toggle_complete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    entry.is_completed = not entry.is_completed
    entry.save()
    return redirect('index')

@login_required
def index(request):
    if request.method == 'POST':
        if not request.user.is_superuser:  # Проверка, чтобы только суперпользователь мог добавлять записи
            return redirect('index')
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EntryForm()
    entries = Entry.objects.all()
    return render(request, 'journal/index.html', {'form': form, 'entries': entries})