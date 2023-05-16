from django import forms 

from .models import Todo


class TodoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Todo
        fields = ('title',)
