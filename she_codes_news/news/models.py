from django.db import models
from django.contrib.auth import get_user_model

class NewsStory(models.Model):
    # It will grab all the data sorted by order 
    # class Meta:
    #   order_by = 'pub_date'
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE
        )
    pub_date = models.DateTimeField()
    content = models.TextField()
