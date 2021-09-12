from django.urls import path
from .views import Myview, MyTemplateView, PostPreLoadTask, SinglePostView
from django.views.generic import TemplateView, RedirectView

app_name = 'MyClass'
urlpatterns = [
    path('', Myview.as_view()),
    # path('h/', TemplateView.as_view(template_name = "about.html", extra_context = {'title': 'custom_title'})),
    path('h/', MyTemplateView.as_view(), name = 'h'),
    path("rdt/", RedirectView.as_view(url = 'https://www.youtube.com/'), name="visit-to-youtube"),
    path("ex3/<int:pk>/", PostPreLoadTask.as_view(), name="redirect-task"),
    path("ex4/<int:pk>/", SinglePostView.as_view(), name="single-task"),


]
