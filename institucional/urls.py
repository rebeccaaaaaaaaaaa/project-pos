from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('team/', views.team, name='team'),
    path('blog/<slug:pk>', views.PostDetail.as_view(), name='post_detail'),


]
