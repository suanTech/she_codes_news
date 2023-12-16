from django import forms
from django.forms import ModelForm
from .models import *

class StoryForm(ModelForm):
  
  class Meta:
    model = NewsStory
    fields = ['title', 'pub_date', 'content', 'image']
    widgets = {
      'pub_date': forms.DateTimeInput(
        format = '%m/%d/%Y',
        attrs = {
          'class': 'form-control',
          'placeholder': 'Select a date',
          'type': 'datetime-local'
        }
      ),
    }

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['pub_date', 'content']
    widgets = {
      'pub_date': forms.DateTimeInput(
        format = '%m/%d/%Y',
        attrs = {
          'class': 'form-control',
          'placeholder': 'Select a date',
          'type': 'datetime-local'
        }
      ),
    }
