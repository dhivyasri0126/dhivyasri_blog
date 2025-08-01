from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    text = models.TextField()
    title = models.CharField(max_length=200)
    theme = models.CharField(max_length=200,default="Default")
    audio_file=models.FileField(upload_to='audio/',blank = True,null =True)
    image = models.ImageField(upload_to='images/',blank=True, null = True)
    video_file = models.FileField(upload_to='videos/',blank=True, null = True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title    

    