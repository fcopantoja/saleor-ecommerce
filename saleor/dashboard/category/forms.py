from django import forms
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.utils.translation import pgettext_lazy
from text_unidecode import unidecode

from saleor.dashboard.product.forms import RichTextField
from ...product.models import Category
from ..seo.fields import SeoDescriptionField, SeoTitleField


class CategoryForm(forms.ModelForm):
    description = RichTextField()

    def __init__(self, *args, **kwargs):
        self.parent_pk = kwargs.pop('parent_pk')
        super().__init__(*args, **kwargs)
        self.fields['description'].label = 'Descripción'
        self.fields['background_image'].label = 'Imagen de fondo'

        self.fields['seo_description'] = SeoDescriptionField(
            extra_attrs={'data-bind': self['description'].auto_id})
        self.fields['seo_title'] = SeoTitleField(
            extra_attrs={'data-bind': self['name'].auto_id})

    class Meta:
        model = Category
        exclude = ['slug']
        labels = {
            'name': pgettext_lazy('Item name', 'Name'),
            'description': pgettext_lazy('Description', 'Descripcion')}

    def save(self, commit=True):
        self.instance.slug = slugify(unidecode(self.instance.name))
        if self.parent_pk:
            self.instance.parent = get_object_or_404(
                Category, pk=self.parent_pk)
        return super().save(commit=commit)
