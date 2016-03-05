from django.db import models
from django.core.urlresolvers import reverse

import markdown2


class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("tag_index", kwargs={"slug": self.slug})


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Post(models.Model):
    title = models.CharField(max_length=255)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    body = models.TextField()
    body_html = models.TextField(editable=False, blank=True, null=True)
    excerpt = models.TextField(blank=True, null=True)
    excerpt_html = models.TextField(editable=False, blank=True, null=True)
    publish = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    objects = PostQuerySet.as_manager()

    def save(self):
        self.body_html = markdown2.markdown(self.body, extras=['fenced-code-blocks'])
        if self.excerpt:
            self.excerpt_html = markdown2.markdown(self.excerpt, extras=['fenced-code-blocks'])
        super(Post, self).save()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ['-date_created']


