from django.shortcuts import render, get_object_or_404
from django.views import generic
from blog.models import BlogItem
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def team(request):
    return render(request, 'team.html')

def blog(request):
    #post_list = BlogItem.objects.all()
    post_list = BlogItem.objects.all()
    paginator = Paginator(post_list, 1)
    page = request.GET.get('blog')
    posts = paginator.get_page(page)
    

    return render(request, 'blog.html', context={'post_list': post_list, 'posts': posts})


class BlogView(ListView):
    model = BlogItem
    template_name = 'blog.html'
    context_object_name = 'post_list'
    

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context
    

class PostDetail(generic.DetailView):
    model = BlogItem
    template_name = 'post_detail.html'


