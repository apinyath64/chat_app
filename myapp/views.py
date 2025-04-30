from django.shortcuts import render, redirect
from .models import ChatRoom, Message


def chat_room(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']

        try:
            rooms = ChatRoom.objects.get(name=room)
        except ChatRoom.DoesNotExist:
            new_room = ChatRoom(name=room)
            new_room.save()
        
        return redirect('room', room=room, username=username)
    
    return render(request, 'index.html')


def message(request, room, username):
    chat_room = ChatRoom.objects.get(name=room)
    messages = Message.objects.filter(room=chat_room)

    return render(request, 'message.html', locals())