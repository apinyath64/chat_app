from django.db import models

class ChatRoom(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return f'{self.room} {self.sender}'
    
