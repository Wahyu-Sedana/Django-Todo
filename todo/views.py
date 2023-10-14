from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from .models import Todo


def index(request):
    items = Todo.objects.order_by('-id')
    return render(request, 'index.html', {'items': items})


def done(request):
    items = Todo.objects.filter(status=True).order_by('-id')
    return render(request, 'index.html', {'items': items})


def pending(request):
    items = Todo.objects.filter(status=False).order_by('-id')
    return render(request, 'index.html', {'items': items})


def delete_all(request):
    Todo.objects.all().delete()
    return HttpResponseRedirect(reverse('index'))


def create(request):
    try:
        title = request.POST['title']
        todo = Todo(title=title)
        todo.save()
        return HttpResponseRedirect(reverse('index'))
    except Exception:
        return HttpResponseRedirect(reverse('index'))


def update(request, id):
    try:
        todo = Todo.objects.get(id=id)
        todo.status = not todo.status
        todo.save()

        return HttpResponseRedirect(reverse('index'))
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    try:
        todo = Todo.objects.get(id=id)
        todo.delete()
        return HttpResponseRedirect(reverse('index'))
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('index'))