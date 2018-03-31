from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime

# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})

def detail(request, my_args):
    post = Article.objects.get(id=int(my_args))
    respon_str = f'tittle = {post.title}, category = {post.category}, \
                    date_time = {post.date_time}, content = {post.content}'
    return HttpResponse(respon_str)

def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})
