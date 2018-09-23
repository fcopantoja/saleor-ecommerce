from django.template.response import TemplateResponse

from .models import Post


def blog_index(request):
    posts = Post.objects.all().order_by('-id')
    return TemplateResponse(request, 'blog/index.html', {'posts': posts})
