from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin


class PostAdmin(MarkdownModelAdmin):
    list_display = ("title", "date_created")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag)
