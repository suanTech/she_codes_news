from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import datetime

class NewsStory(models.Model):
    # It will grab all the data sorted by order 
    # class Meta:
    #   order_by = 'pub_date'
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE
        )
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    content = models.TextField()
    image = models.URLField(null=True, blank=True)

class Comment(models.Model):
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE
        )
    pub_date = models.DateTimeField()
    content = models.TextField()
    story = models.ForeignKey(
        NewsStory,
        related_name='comments',
        on_delete=models.CASCADE
    )