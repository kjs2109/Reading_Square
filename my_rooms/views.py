from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from my_rooms.models import Book
from users.models import User
from my_rooms.forms import BookStatusForm, BookForm 

# Create your views here.
def books(request, user_id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=user_id)
        befor_read_books = Book.objects.filter(Q(user=user) & Q(status=1))
        reading_books = Book.objects.filter(Q(user=user) & Q(status=2))
        after_read_books = Book.objects.filter(Q(user=user) & Q(status=3))
        
        form = BookStatusForm()

        context = {
            'before_read_books': befor_read_books,
            'reading_books': reading_books,
            'after_read_books': after_read_books,
            'form': form,
        }
        return render(request, 'my_rooms/my_room.html', context)

    else:
        return render(request, 'users/login_required.html')

def edit_book_status(request, user_id, book_id):
    if request.user.is_authenticated:
        book = get_object_or_404(Book, pk=book_id)
        if request.method == 'POST':
            form = BookStatusForm(request.POST)
            if form.is_valid():
                book.status = form.cleaned_data['status']
                book.save()
        return redirect('my_rooms:books', user_id=user_id)
    else:
        return render(request, 'users/login_required.html')

def add_book(request, user_id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = BookForm()

        elif request.method == 'POST':
            form = BookForm(request.POST, request.FILES)
            if form.is_valid():
                new_book = form.save(commit=False)
                new_book.user = request.user 
                new_book.save()
                return redirect('my_rooms:books', user_id=user_id)

        return render(request, 'my_rooms/book_input_form.html', {'form': form})

    else:
        return render(request, 'users/login_required.html')