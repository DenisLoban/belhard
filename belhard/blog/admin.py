from django.contrib import admin
from django.contrib.admin import StackedInline

from .models import Category, Post, Portfolio, Team

class PostInleneModelAdmin(StackedInline):
    model = Post
    can_delete = False
@admin.action(description='Опубликовать пост')
def make_published(request, model, queryset):
    queryset.update(is_published=True)

@admin.action(description='Снать с публикации')
def make_unpublished(request, model, queryset):
    queryset.update(is_published=False)

# admin.site.register(Category)
# admin.site.register(Post)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)
    inlines = (PostInleneModelAdmin, )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('category', 'author')
    search_fields = ('title', 'body')
    date_hierarchy = 'date_created'
    prepopulated_fields = {'slug': ('title', )}
    readonly_fields = ('date_created', )
    actions = (make_unpublished, make_published)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass

