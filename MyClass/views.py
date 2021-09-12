from django.db.models.query_utils import PathInfo
from MyClass.models import Post
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import RedirectView, TemplateView
from django.db.models import F

# Create your views here.

class Myview(View):

    greetings = "Devansh Sharma"

    def get(self, request):
        return HttpResponse(self.greetings)

# TemplateView Example

class MyTemplateView(TemplateView):
    template_name = "example2.html"
    # template_engine = "Jinja"
    # response_class = "Custom template loading or custom context object instantiation"
    # content_type = "Default Django uses text.html"

    # get_context_data(**kwarg) is a method inherited from Content Mixin
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Post.objects.get(id = 1)
        for i in Post.objects.all():
            a = i.author
        context['author'] = a

        return context

class PostPreLoadTask(RedirectView):
    # url = 'https://www.youtube.com/'
    pattern_name = 'MyClass:singlepost' # Used for redirects
    # parmanent = HTTP status code returned (True = 301, False = 302, Default = False)

    def get_redirect_url(self, *args, **kwargs):
        # post = get_object_or_404(Post, pk = kwargs['pk'])
        #post.count += 1
        #post.count

        post = Post.objects.filter(pk = kwargs['pk'])
        post.update(count = F('count') + 1)


class SinglePostView(TemplateView):
    template_name = "example3.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = get_object_or_404(Post, pk = self.kwargs.get('pk'))
        return context

