from .models import Micro
from django.forms import ModelForm, TextInput, Textarea

class MicroForm(ModelForm):
    class Meta:
        model = Micro
        fields = ["title", "micro"]
        widgets = {
            "title": TextInput(attrs={'class': 'form-control','placeholder': 'Введите название'}),
            "micro": Textarea(attrs={'class': 'form-control','placeholder': 'Введите описание'})
            }