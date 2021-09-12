from typing import Counter
from Books.models import Books
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView
from .forms import AddForm
from django.db.models import F
from django.utils import timezone


# Create your views here.

# Creating list views
class BookListView(ListView):
    model = Books
    template_name = 'home.html'
    queryset = Books.objects.all()
    context_object_name = 'books'
    paginate_by = 4
    # queryset = Books.objects.all()[:2]

    def get_queryset(self):
        return Books.objects.all()[:3]

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(*kwargs)
    #     context['books'] = Books.objects.all()
    #     return context

# class IndexView(TemplateView):
#     template_name = 'home.html'
    
#     def get_context_data(self, **kwargs):
#         print("hello")
#         context = super().get_context_data(**kwargs)
#         context['books'] = Books.objects.all()
        
#         return context


class GenreView(ListView):
    model = Books
    template_name = 'home.html'
    context_object_name = 'books'
    paginate_by = 4

    def get_queryset(self):
        return Books.objects.filter(genre__icontains = self.kwargs.get('genre'))

# Detail View Example
class BookDetailView(DetailView):
    model = Books
    template_name = 'book-detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # filtering the data using the Slug from the 
        post = Books.objects.filter(slug = self.kwargs.get('slug'))
        post.update(count = F('count') + 1)

        context['time'] = timezone.now()

        return context

# class AddBookView(FormView):
#     template_name = 'add.html'
#     form_class = AddForm
#     success_url = '/books/'

#     # allows us to create the new objects
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class CreateBookView(CreateView):
    model = Books
    template_name = 'add.html'
    form_class = AddForm
    success_url = '/books/'

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        initial['title'] = 'Enter Title'

        return initial


class BookEditView(UpdateView):
    model = Books
    template_name = 'add.html'
    form_class = AddForm
    success_url = '/books/'