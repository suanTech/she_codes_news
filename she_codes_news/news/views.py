from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import NewsStory
from .forms import *

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        return context
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commentform"] = CommentForm()
        author = self.object.author
        other_stories = NewsStory.objects.filter(author=author).exclude(id=self.object.id)

        context['other_stories'] = other_stories
        return context


class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_objcet_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    def form_valid(self, form):
        form.instance.author = self.request.user
        pk = self.kwargs.get('pk')
        return super().form_valid(form)


class EditStoryView(generic.UpdateView):
    model = NewsStory
    form_class = StoryForm
    context_objcet_name = 'storyform'
    template_name = 'news/editStory.html'
    success_url = reverse_lazy('news:index')

class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')

class AddCommentView(generic.CreateView):
    form_class = CommentForm
    template_name = 'news/story.html'
    success_url = reverse_lazy('news:index')
    def form_valid(self, form):
        form.instance.author = self.request.user
        pk = self.kwargs.get('pk')
        form.instance.story = get_object_or_404(NewsStory, pk=pk)
        return super().form_valid(form)