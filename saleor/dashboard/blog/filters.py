from django.utils.translation import npgettext, pgettext_lazy
from django_filters import CharFilter, OrderingFilter

from ...core.filters import SortedFilterSet
from ...blog.models import Post

SORT_BY_FIELDS = {
    'title': pgettext_lazy('Post list sorting option', 'title'),
    'created_on': pgettext_lazy('Post list sorting option', 'created_on'),
}


class PostFilter(SortedFilterSet):
    title = CharFilter(
        label=pgettext_lazy('Category list filter label', 'Title'),
        lookup_expr='icontains')
    sort_by = OrderingFilter(
        label=pgettext_lazy('Category list sorting filter label', 'Sort by'),
        fields=SORT_BY_FIELDS.keys(),
        field_labels=SORT_BY_FIELDS)

    class Meta:
        model = Post
        fields = []

    def get_summary_message(self):
        counter = self.qs.count()
        return npgettext(
            'Number of matching records in the dashboard posts list',
            'Found %(counter)d matching posts',
            'Found %(counter)d matching posts',
            number=counter) % {'counter': counter}
