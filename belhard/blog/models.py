from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='названия',
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Post(models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name='заголовок'
    )
    body = models.TextField(
        verbose_name='пост'
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name='категория'
    )
    date_created = models.DateTimeField(
        verbose_name='дата создания',
        default=now
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор'
    )
    is_published= models.BooleanField(
        default=False,
        verbose_name='публикация')

    @property
    def date(self):
        return self.date_created.strftime('%d.%m.%Y %H:%M')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog_post_detail', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
