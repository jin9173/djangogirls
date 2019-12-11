from django.shortcuts import render

from blog.models import Post


def post_list(request):
    # Template을 찾을 경로에서
    #   post_list.html을 찾아서
    #   그 파일을 text로 만들어서 HttpResponse형태로 돌려준다
    # 위 기능을 하는 shortcut함수

    # 실제 render함수의 역할
    #   content = loader.render_to_string('post_list.html', None, request)
    #   return HttpResponse(content)

    # 1. posts라는 변수에 전체 Post를 가지는 QuerySet객체를 할당
    #    hint) Post.objects.무언가....를 실행한 결과는 QuerySet객체가 된다
    # 2. context라는 dict를 생성하며, 'posts'키에 위 posts변수를 value로 사용하도록 한다
    # 3. render의 3번째 위치인자로 위 context변수를 전달한다
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)





# settings.py에서 경로설정
# views.py에서 render함
#   어디서 하든 무방하지만 djangogirls 규칙 (MTV)

# import os
#
# from django.core.checks import templates
# from django.http import HttpResponse
# from django.shortcuts import render
#
#
# def post_list(request):
#     # 상위폴더(blog)의
#     #   상위폴더(djangogirls)의
#     #       하위폴더(templates)
#     #           하위파일(post_list.html)내용을 read()한 결과를 HttpResponse에 인자로 전달
#
#     # 경로이동
#     #   os.path.abspath(__file__) <- 현재 파일의 절대 경로를 리턴해줌
#     #   os.path.dirname
#     #   os.path.join
#
#     # 파일 열기
#     #   open
#     cur_file_path = os.path.abspath(__file__)
#     blog_dir_path = os.path.dirname(cur_file_path)
#     # 절대 경로를 사용할 경우 운영체제마다 path 작성 방식이 다르기 때문에 깨질 수도 있다
#     # print(blog_dir_path)
#     # path = blog_dir_path + '/../templates/post_list.html'
#     # print(path)
#     root_dir_path = os.path.dirname(blog_dir_path)
#     templates_dir_path = os.path.join(root_dir_path, 'templates')
#     post_list_html_path = os.path.join(templates_dir_path, 'post_list.html')
#
#     f = open(post_list_html_path, 'rt')
#     html = f.read()
#     f.close()
#
#     return HttpResponse(html)
