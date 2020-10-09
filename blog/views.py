from django.shortcuts import render, get_object_or_404
from . import models

def blogposts(request):
    posts = models.blog.objects
    return render(request, "blog/blogposts.html", {"posts" : posts})

def detail(request, blog_id):
    blog = get_object_or_404(models.blog, pk=blog_id)
    return render(request, "blog/detail.html",{"blog" : blog})