from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.blog_index, name='index'),
    # url(r'^(?P<pk>[0-9]+)/$',
    #     views.category_details, name='category-details'),
]
