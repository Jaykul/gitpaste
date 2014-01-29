from haystack.indexes import *
from models import Paste, Commit


class CommitIndex(SearchIndex, Indexable):
    text = CharField(document=True, use_template=True)
    commit = CharField(model_attr='commit')
    user = CharField(model_attr='owner', null=True)

    def get_model(self):
        return Commit

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class PasteIndex(SearchIndex, Indexable):
    text = CharField(document=True, use_template=True)
    paste = CharField(model_attr='paste')
    filename = CharField(model_attr='filename')
    language = CharField(model_attr='language')
    commit = CharField(model_attr='revision')
    #user = CharField(model_attr='revision')

    def get_model(self):
        return Paste

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
