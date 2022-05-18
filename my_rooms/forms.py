from django import forms 
from .models import Book

class BookStatusForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = ['status']
        # widgets = {
        #     'status': forms.Select,
        # }



class BookForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = ['title', 'author', 'memo', 'book_image']
        widgets = {
            'memo': forms.Textarea,
        }