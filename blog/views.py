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
    # request.POST에 담긴 title, text를
    # HTTPResponse를 사용해서 적절히 리턴
    #   title: <입력받은 제목>, text: <입력받은 텍스트>
    # 위와 같은 문자열을 리턴해주도록 한다

    # title = request.POST['title']
    # text = request.POST['text']
    # print(title, text)

    if request.method == 'POST':
        author = request.user
        title = request.POST['title']
        text = request.POST['text']

        # 위 3개의 값을 사용해서
        # 새로운 Post를 생성
        # 생성한 Post의 title과 created_date를 HttpResponse에 적절한 문자열로 전달
        #   출력 예) title: 파이썬, created_date: <적당한 값>

        post = Post.objects.create(
            author=author,
            title=title,
            text=text,
        )
        result = f'title: {post.title}, created_date: {post.created_date}'
        return HttpResponse(result)
    else:
        return render(request, 'post_add.html')
