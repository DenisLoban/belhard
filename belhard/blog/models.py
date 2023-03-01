from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='названия', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Post(models.Model):
    title = models.CharField(max_length=64, verbose_name='заголовок')
    body = models.TextField(verbose_name='пост')
    slug = models.SlugField(verbose_name='URL', unique=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='категория')
    date_created = models.DateTimeField(verbose_name='дата создания', default=now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')
    is_published = models.BooleanField(default=False, verbose_name='публикация')

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


class Portfolio(models.Model):
    title = models.CharField(max_length=64, verbose_name='заголовок')
    subtitle = models.CharField(max_length=64, verbose_name='подзаголовок')
    description = models.CharField(max_length=2048, verbose_name='описание')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='картинка', upload_to='portfolio/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'портфолио'
        verbose_name_plural = 'портфолио'


class Team(models.Model):
    name = models.CharField(max_length=64, verbose_name='имя')
    surname = models.CharField(max_length=64, verbose_name='фамилия')
    job_title = models.CharField(max_length=64, verbose_name='должность')
    #twitter = models.CharField(max_length=64, verbose_name='ссылка на Twitter')
    #facebook = models.CharField(max_length=64, verbose_name='ссылка на Facebook')
    #instagram = models.CharField(max_length=64, verbose_name='ссылка на Instagram')
    image = models.ImageField(verbose_name='фото', upload_to='team/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'команда'
        verbose_name_plural = 'команды'
