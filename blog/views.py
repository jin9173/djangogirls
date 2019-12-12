from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)


def post_detail(request, pk):
    print('post_detail request', request)
    print('post_detail pk', pk)

    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse('없음')

    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)
