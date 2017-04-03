from haystack.views import SearchView

from blog.models import Article, Category, Tag


class MySearchView(SearchView):
    template_name = "index.html"
    context_object_name = "article_list"

    def extra_context(self):
        context = super(MySearchView, self).extra_context()
        context['category_list'] = Category.objects.all()
        context['date_archive'] = Article.objects.archive()
        context['tag_list'] = Tag.objects.all()
        return context


