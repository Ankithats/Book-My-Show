from django.db import models
class Movie(models.Model):
    name=models.CharField(max_length=250)
    rating=models.FloatField()
    type=models.TextField()
    language=models.TextField()
    category=models.TextField()
    duration=models.TextField()
    certificate=models.TextField()
    date=models.DateField()
    banner=models.ImageField(upload_to='todoimage')
    poster=models.ImageField(upload_to='todoimage')
    
    
    def __str__(self):
        return self.name
