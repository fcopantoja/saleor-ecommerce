import re

from django.db import models
from django.utils.translation import pgettext_lazy
from versatileimagefield.fields import VersatileImageField

from ..seo.models import SeoModel
from ..account.models import User


class Post(SeoModel):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    image = VersatileImageField(upload_to='blog-images', blank=True, null=True)

    class Meta:
        app_label = 'blog'
        permissions = (
            ('view_post',
             pgettext_lazy('Permission description', 'Can view post')),
            ('edit_post',
             pgettext_lazy('Permission description', 'Can edit post')))

    def __str__(self):
        return self.title

    def get_summary(self):
        cleanr = re.compile('<.*?>')
        clean_text = re.sub(cleanr, '', self.content)
        return (clean_text[:300] + '...') if len(clean_text) > 300 else clean_text

    # def get_absolute_url(self, ancestors=None):
    #     return reverse('product:category',
    #                    kwargs={'path': self.get_full_path(ancestors),
    #                            'category_id': self.id})
    #
    # def get_full_path(self, ancestors=None):
    #     if not self.parent_id:
    #         return self.slug
    #     if not ancestors:
    #         ancestors = self.get_ancestors()
    #     nodes = [node for node in ancestors] + [self]
    #     return '/'.join([node.slug for node in nodes])
