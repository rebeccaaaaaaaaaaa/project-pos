from django.shortcuts import render, get_object_or_404
from django.views import generic
from blog.models import BlogItem
from django.views.generic import ListView, DetailView

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def team(request):
    return render(request, 'team.html')

def blog(request):
    post_list = BlogItem.objects.all()
    return render(request, 'blog.html', context={'post_list': post_list})


class BlogView(ListView):
    model = BlogItem
    template_name = 'blog.html'
    context_object_name = 'post_list'
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['title'] = 'Blog'
        paginators = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginators, page, is_paginated)
        context.update(pagination_data)
        return context
    
