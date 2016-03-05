from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views import generic
from django.shortcuts import render

from . import models


def blog_index(request, tag=None, num_posts=5):
    if tag:
        posts = models.Post.objects.filter(publish=True).filter(tags__slug=tag)
    else:
        posts = models.Post.objects.filter(publish=True)
    paginator = Paginator(posts, num_posts)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'post_list.html', {'post_list': post_list})


class BlogDetail(generic.DetailView):
    model = models.Post
    template_name = 'post.html'
    queryset = models.Post.objects.filter(publish=True)


@login_required
def draft_list(request):
    posts = models.Post.objects.filter(publish=False)
    template_name = 'draft_list.html'
    return render(request, template_name, {'post_list': posts})


class TagIndex(generic.ListView):
    template_name = 'post_list.html'
    paginate_by = 5

    def get_queryset(self):
        slug = self.kwargs['slug']
        tag = models.Tag.objects.get(slug=slug)
        results = models.Post.objects.filter(tags=tag).filter(publish=True)
        return results
