from django.http import HttpResponse
from django.shortcuts import render

rooms = [
    {'id': 1, 'name': "Check 1"},
    {'id': 2, 'name': "Two"},
    {'id': 3, 'name': "Top 3"}
]


def home(request):
    context = {'rooms':rooms}
    return render(request, "base/home.html", context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}
    return render(request, 'base/room.html', context)
