from django import forms
from django.utils.text import slugify
from django.utils.translation import pgettext_lazy
from text_unidecode import unidecode

from saleor.dashboard.product.forms import RichTextField
from ...blog.models import Post
from ..seo.fields import SeoDescriptionField, SeoTitleField


class PostForm(forms.ModelForm):
    content = RichTextField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['seo_description'] = SeoDescriptionField(
            extra_attrs={'data-bind': self['content'].auto_id})
        self.fields['seo_title'] = SeoTitleField(
            extra_attrs={'data-bind': self['title'].auto_id})

    class Meta:
        model = Post
        exclude = ['slug', 'user']
        labels = {
            'title': pgettext_lazy('Item name', 'Title'),
            'created_on': pgettext_lazy('Fecha', 'Fecha')}

    def save(self, commit=True):
        self.instance.slug = slugify(unidecode(self.instance.title))
        return super().save(commit=commit)
