from django.shortcuts import render
from .models import Room
# Create your views here.

# da_rooms = [
#     {'id': 1, 'name': 'Lets learn python!'},
#     {'id': 2, 'name': 'design!'},
#     {'id': 3, 'name': 'frontend!'},
#     {'id': 4, 'name': 'backend!'},
# ]

def home(request):
    da_rooms = Room.objects.all()   # just like SQL to select all
    context = {'rooms': da_rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    da_rooms = Room.objects.get(id=pk)
    context = {'room': da_rooms}
    return render(request, 'base/room.html', context)
