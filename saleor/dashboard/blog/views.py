from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils.translation import pgettext_lazy

from ...core.utils import get_paginator_items
from ...blog.models import Post
from ..views import staff_member_required
from .filters import PostFilter
from .forms import PostForm


@staff_member_required
@permission_required('blog.view_post')
def post_list(request):
    posts = Post.objects.all().order_by('title')
    post_filter = PostFilter(request.GET, queryset=posts)
    posts = get_paginator_items(
        post_filter.qs, settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page'))
    ctx = {
        'posts': posts, 'filter_set': post_filter,
        'is_empty': not post_filter.queryset.exists()}
    return TemplateResponse(request, 'dashboard/blog/list.html', ctx)


@staff_member_required
@permission_required('blog.edit_post')
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(
            request,
            pgettext_lazy(
                'Dashboard message', 'Entrada agregada %s') % post.title)
        return redirect('dashboard:post-list')
    ctx = {'form': form}
    return TemplateResponse(request, 'dashboard/blog/form.html', ctx)


@staff_member_required
@permission_required('blog.edit_post')
def post_edit(request, pk=None):
    blog_post = get_object_or_404(Post, pk=pk)
    form = PostForm(
        request.POST or None, instance=blog_post)
    status = 200
    if form.is_valid():
        blog_post = form.save()
        messages.success(
            request,
            pgettext_lazy(
                'Dashboard message', 'Entrada actualizada %s') % blog_post.title)
        return redirect('dashboard:post-list')
    elif form.errors:
        print(form.errors)
        status = 400
    ctx = {'post': blog_post, 'form': form, 'status': status}
    template = 'dashboard/blog/form.html'
    return TemplateResponse(request, template, ctx, status=status)
#
#
# @staff_member_required
# @permission_required('product.view_category')
# def category_details(request, pk):
#     root = get_object_or_404(Category, pk=pk)
#     path = root.get_ancestors(include_self=True) if root else []
#     categories = root.get_children().order_by('name')
#     category_filter = CategoryFilter(request.GET, queryset=categories)
#     categories = get_paginator_items(
#         category_filter.qs, settings.DASHBOARD_PAGINATE_BY,
#         request.GET.get('page'))
#     ctx = {'categories': categories, 'path': path, 'root': root,
#            'filter_set': category_filter,
#            'is_empty': not category_filter.queryset.exists()}
#     return TemplateResponse(request, 'dashboard/category/detail.html', ctx)
#
#
# @staff_member_required
# @permission_required('product.edit_category')
# def category_delete(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     if request.method == 'POST':
#         category.delete()
#         messages.success(
#             request,
#             pgettext_lazy(
#                 'Dashboard message', 'Removed category %s') % category)
#         root_pk = None
#         if category.parent:
#             root_pk = category.parent.pk
#         if root_pk:
#             if request.is_ajax():
#                 response = {'redirectUrl': reverse(
#                     'dashboard:category-details', kwargs={'pk': root_pk})}
#                 return JsonResponse(response)
#             return redirect('dashboard:category-details', pk=root_pk)
#         else:
#             if request.is_ajax():
#                 response = {'redirectUrl': reverse('dashboard:category-list')}
#                 return JsonResponse(response)
#             return redirect('dashboard:category-list')
#     ctx = {'category': category,
#            'descendants': list(category.get_descendants()),
#            'products_count': len(category.products.all())}
#     return TemplateResponse(
#         request, 'dashboard/category/modal/confirm_delete.html', ctx)
