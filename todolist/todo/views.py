from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ListItem


def todoView(request):
    all_items = ListItem.objects.all()
    completed_items = ListItem.objects.all().filter(is_done=True)
    return render(request, 'todo.html',
                  {'all_items': all_items, 'completed_items': completed_items})


def addTodo(request):
    new_item = ListItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
    delete_item = ListItem.objects.get(id=todo_id)
    delete_item.delete()
    return HttpResponseRedirect('/todo/')


def completeTodo(request, todo_id):
    complete_item = ListItem.objects.get(id=todo_id)
    complete_item.is_done = True
    complete_item.save()
    return HttpResponseRedirect('/todo/')



