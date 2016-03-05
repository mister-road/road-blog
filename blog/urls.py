from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_index, name="index"),
    url(r'^code$', views.blog_index, name="code_index", kwargs={'tag': 'code'}),
    url(r'^FIRE$', views.blog_index, name="FIRE_index", kwargs={'tag': 'FIRE'}),
    url(r'^drafts$', views.draft_list, name="draft_index"),
    url(r'^post/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
    url(r'^tag/(?P<slug>\S+)$', views.TagIndex.as_view(), name="tag_index"),
]
