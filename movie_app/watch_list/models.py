from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    website = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class WatchList(models.Model):
    platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name='watch_list')
    title = models.CharField(max_length=50)
    storyline = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Review(models.Model):
      ratings = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
      description = models.CharField(max_length=200,null=True)
      active = models.BooleanField(default=True)
      watchlist = models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name='review')
      created = models.DateTimeField(auto_now_add=True)
      updated = models.DateTimeField(auto_now=True)
      
      def __str__(self):
          return str(self.ratings) + " " + self.watchlist.title
    