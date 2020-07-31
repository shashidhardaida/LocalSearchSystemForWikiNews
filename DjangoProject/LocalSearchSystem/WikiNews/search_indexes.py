from .models import WikiNewsItem
from haystack import indexes


class WikiNewsItemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    id = indexes.IntegerField(model_attr='id')

    def get_model(self):
        return WikiNewsItem

    def index_queryset(self, using=None):
        return self.get_model().objects.all()