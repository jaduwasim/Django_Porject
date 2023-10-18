from django.db import models

class MeetingRoom(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Event(models.Model):
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.room} - {self.start_time} to {self.end_time}"
