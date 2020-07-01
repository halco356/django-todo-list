from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ListItem


def todoView(request):
    all_items = ListItem.objects.all()
    return render(request, 'todo.html',
                  {'all_items': all_items})


def addTodo(request):
    new_item = ListItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')
