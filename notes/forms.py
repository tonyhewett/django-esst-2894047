from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'content': forms.Textarea(attrs={'class': 'form-control mb5'})
        }

        labels = {
            'title': 'Title',
            'content': 'Add your notes here',
        }

    def clean_title(self):    
        title = self.cleaned_data['title']
        if len(title) < 5:  
            raise ValidationError("Title must be at least 5 characters long")
        if len(title) > 20:
            raise ValidationError("Title must be at most 20 characters long")
        """if "Django" not in title:
            raise ValidationError("Title must contain the word 'Django'")"""
        return title
