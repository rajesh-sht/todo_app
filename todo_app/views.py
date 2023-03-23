from django.shortcuts import render, HttpResponseRedirect
from .models import *
# CRUD
# C - Create
# R - Retrieve, Read
# U - Update
# D - Delete


def todo_list(request):
    todos = Todo.objects.all()

    return render(
        request=request,
        template_name="bootstrap/todo_list.html",
        context={"todos": todos},
    )


def todo_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        # ORM => Object Relational Mapping
        Todo.objects.create(title=title)
        return HttpResponseRedirect("/")
    return render(request, 'bootstrap/todo_create.html')


def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)  # pk is primary key(id)
    todo.delete()
    return HttpResponseRedirect('/')


def todo_update(request, pk):
    todo = Todo.objects.get(pk=pk)  # fetch only one
    if request.method == "POST":
        title = request.POST['title']
        todo.title = title
        todo.save()
        return HttpResponseRedirect('/')
    else:
        return render(
            request,
            'bootstrap/todo_update.html',
            {"todo": todo},)
