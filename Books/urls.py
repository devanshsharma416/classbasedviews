from django.conf.urls import url
from django.urls import path
from .views import BookListView, BookDetailView, GenreView, CreateBookView, BookEditView

app_name = 'Books'
urlpatterns = [

    # path("index", IndexView.as_view(), name="index"),
    path("", BookListView.as_view(), name="book-list"),
    path("g/<str:genre>", GenreView.as_view(), name=""),
    # path("add", AddBookView.as_view(), name="add-book"),
    path("create", CreateBookView.as_view(), name="create-book"),
    path("<slug:slug>", BookDetailView.as_view(), name="book-detail"),
    path("<slug:slug>/edit", BookEditView.as_view(), name="book-edit")
    
]
