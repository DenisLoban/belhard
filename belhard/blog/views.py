from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.views.decorators.http import require_GET
from django.views.generic import ListView, DetailView
# from slugify import slugify
from slugify import slugify
from .forms import PostModelForm

from .models import Post, Portfolio, Team


class PostListView(ListView):
    model = Portfolio
    context_object_name = 'portfolio_items'
    template_name = 'blog/index.html' #формируется атоматически и потом поменяли на блог.индекс
    http_method_names = ('get', 'post')  # переопределение для ускорения работы вместо списка- кортеж

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListView, self).get_context_data()
        context['post_form'] = PostModelForm()
        return context

    def post(self, request: HttpRequest):
        data = request.POST.dict()
        data.update(slug=slugify(request.POST.get('title')))
        form = PostModelForm(data)
        if form.is_valid():
            form.save()
        return self.get(request=request)

    def get_queryset(self):
        return Portfolio.objects.all()


class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = 'post_slug'
    http_method_names = ('get', )

    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg)
        return get_object_or_404(self.model, Q(slug=slug) & Q(is_published=True))

    def get(self, *args, **kwargs):
        obj = self.get_object()
        text = f'<b>{obj.title}</b></br><b>{obj.body}</b>'
        return HttpResponse(text)

    def page_not_found(request, exception):
        print(exception)
        return HttpResponse('<b>404 PAGE NOT FOUND</b>')


# def get(self, request, *args, **kwargs):
#     posts = self.get_queryset()
#     text = ''
#     for post in posts:
#         text += f'<a href="{post.get_absolute_url()}">{post.title}</a></br>'
#     return HttpResponse(text)

# @require_GET
# def post_list(requests: HttpRequest):
#     posts = Post.objects.all()
#     text = ''
#     for post in posts:
#         text += f'<a href="{post.get_absolute_url()}">{post.title}</a></br>'
#     return HttpResponse(text)

# @require_GET
# def post_detail(requests: HttpRequest, post_slug: str):
#     # post = Post.objects.get(slug=post_slug)
#     post = get_object_or_404(Post, slug=post_slug)
#     text = f'<b>{post.title}</b></br><b>{post.body}</b>'
#     return HttpResponse(text)
