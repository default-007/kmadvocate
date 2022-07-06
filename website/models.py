from email.mime import image
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.shortcuts import reverse


class Service(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.ImageField(blank=True, null=True)
    description = MarkdownxField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("website:services", args=[str(self.id)])

    def formatted_markdown(self):
        return markdownify(self.description)

    def body_summary(self):
        return markdownify(self.description[:200] + "...")

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = "/static/images/coming.jpg"
        return url


class BlogCategory(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(
        BlogCategory, on_delete=models.CASCADE, blank=True, null=True
    )
    author = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    text = MarkdownxField()
    quote = MarkdownxField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("website:blog", args=[str(self.id)])

    def formatted_markdown(self):
        return markdownify(self.text)

    def body_summary(self):
        return markdownify(self.text[:200] + "...")

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = "/static/images/coming.jpg"
        return url


class Partner(models.Model):
    names = models.CharField(max_length=255, blank=True)
    position = models.CharField(max_length=255, blank=True)
    image = models.ImageField(max_length=255, blank=True)
    text = MarkdownxField()
    email = models.EmailField(max_length=255, blank=True)
    facebook_url = models.URLField(max_length=255, blank=True)
    twitter_url = models.URLField(max_length=255, blank=True)
    instagram_url = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return self.names

    def get_absolute_url(self):
        return reverse("website:team", args=[str(self.id)])

    def formatted_markdown(self):
        return markdownify(self.text)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = "/static/images/coming.jpg"
        return url
