from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.name

class Event(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='events',blank=True, null=True)
    poster=models.ImageField(upload_to='event_posters', blank=True, null=True)
    location_name=models.CharField(max_length=255)
    registration_link=models.URLField(blank=True, null=True)
    publish=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True,null=False)
    timings=models.DateTimeField(null=True)
    latitude=models.FloatField(blank=True, null=True)
    longitude=models.FloatField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = 'Events'
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name='comments')
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.created_by.username)