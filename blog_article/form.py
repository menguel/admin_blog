from .models import Artblog
from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Artblog
        fields = '__all__'