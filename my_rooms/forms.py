from django import forms 
from .models import Book

class BookStatusForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = ['status']



class BookForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = ['title', 'author', 'memo', 'book_image']
        widgets = {
            'memo': forms.Textarea,
        }