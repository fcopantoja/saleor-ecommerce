from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.post_list, name='post-list'),
    # url(r'^(?P<pk>[0-9]+)/$',
    #     views.category_details, name='category-details'),
    url(r'^add/$',
        views.post_create, name='blog-post-add'),
    # url(r'^(?P<root_pk>[0-9]+)/add/$',
    #     views.category_create, name='category-add'),
    url(r'^(?P<pk>[0-9]+)/edit/$',
        views.post_edit, name='blog-post-edit'),
    # url(r'^(?P<pk>[0-9]+)/delete/$',
    #     views.category_delete, name='category-delete')
]
