from django.forms import ModelForm, Select, TextInput, Textarea, ChoiceField
from .models import Post


class PostModelForm(ModelForm):
    # title = TextInput(
    #     attrs={
    #         'class': 'form-control',
    #         'id': 'title',
    #         'placeholder': 'Enter Post Title'}
    # )

    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'author', 'slug')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Enter Post Title'}),
            'body': Textarea(attrs={'class': 'form-control', 'id': 'body', 'placeholder': 'Enter Post Body'}),
            'author': Select(attrs={'class': 'form-control', 'id': 'author'}),
            'category': Select(attrs={'class': 'form-control', 'id': 'category'}),
            'slug': TextInput(attrs={'required': False, 'hidden': True, 'id': 'slug', 'value': ' '})
        }
