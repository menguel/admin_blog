from django import forms
from .models import Articles

class ArticleForm(forms.ModelForm):
    name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            'placeholder' : 'votre nom ici'
        }
    ))
    description = forms.CharField(label='', widget=forms.Textarea(
        attrs={
            'placeholder' : 'Enter Article description',
            'rows':5,
            'cols':10,
            'class' : 'exampleFormControlTextarea1',
            'id' : 'myId'
        }
    ))
    like = forms.DecimalField(label='', initial=50)
    actif = forms.BooleanField()
    class Meta:
        model = Articles
        fields = ('name', 'description', 'like', 'image', 'actif')

    def clean_name(self, *args, **kwargs):
            name = self.cleaned_data.get('name')
            if 'uba' in name:
                return name
            else:
                raise forms.ValidationError('Le mot uba doit apparaitre dans votre nom')
    
    
class RowArticleForm(forms.Form):
    name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            'placeholder' : 'votre nom ici'
        }
    ))
    description = forms.CharField(label='', widget=forms.Textarea(
        attrs={
            'placeholder' : 'Enter Article description',
            'rows':5,
            'cols':10,
            'class' : 'm1 m2 m3',
            'id' : 'myId'
        }
    ))
    like = forms.DecimalField(label='', initial=50)
    actif = forms.BooleanField()