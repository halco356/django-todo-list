from django.shortcuts import render
from django.http import HttpResponse
from .models import ListItem


def todoView(request):
    all_items = ListItem.objects.all()
    return render(request, 'todo.html',
                  {'all_items': all_items})


