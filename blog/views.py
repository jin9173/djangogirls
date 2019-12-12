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
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse('없음')

    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)


def post_add(request):
    # URL:      /posts/add
    # View:     이 함수
    # Template: post_add.html
    #   form태그 내부에
    #       input한개, textarea한개, button[type=submit]한개

    # base.html의 nav안에 /posts/add/로의 링크 하나 추가
    #   링크 텍스트: Post Add
    return render(request, 'post_add.html')
