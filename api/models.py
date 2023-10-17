import uuid
from django.db import models


class Movie(models.Model):
    Name = models.CharField(max_length=100, blank = False, null=False)
    Date = models.DateField(blank=False, null=False)
    Time = models.TimeField(blank=False, null=False)
    Seat_count = models.IntegerField(max_length=4, blank=False, null=False)
    Image = models.CharField(max_length=250,blank=False, null=False)
    Director = models.CharField(max_length=100, blank = False, null=False)
    Actors = models.CharField(max_length=100, blank = False, null=False)
    Language = models.CharField(max_length=100, blank = False, null=False)

    class Meta:
        ordering  = ['Name']
    
    def __str__(self):
        return self.Name

class usermodel(models.Model):
    Ticket_id = models.UUIDField( default = uuid.uuid4 )
    Movie_Name = models.CharField(max_length=100, blank = False, null=False)
    Date = models.DateField(blank=False, null=False)
    Time = models.TimeField(blank=False, null=False)
    Seat_count = models.IntegerField(max_length=4, blank=False, null=False)
    User_name = models.CharField(max_length=100, blank = False, null=False, default='no name')

    class Meta:
        ordering = ['Date', 'Time']

    def __str__(self):
        return self.Movie_Name