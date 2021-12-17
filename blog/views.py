from django.views import generic
from .models import BlogItem

class BlogItemList(generic.ListView):
    queryset = BlogItem.objects.all()
    template_name = 'blog.html'

class BlogItemDetail(generic.DetailView):
    model = BlogItem
    template_name = 'blog_detail.html' 