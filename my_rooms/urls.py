from django.urls import path 
from . import views 

app_name = 'my_rooms'
urlpatterns = [
    # my_room/1/books/
    path('<int:user_id>/books/', views.books, name='books'),
    # my_room/1/book_status/1/
    path('<int:user_id>/book_status/<int:book_id>/', views.edit_book_status, name='edit_book_status'),
    # my_room/1/add_book/ 
    path('<int:user_id>/add_book/', views.add_book, name='add_book'),
    # my_room/1/edit_book/1/
    path('<int:user_id>/memo/<int:book_id>/', views.edit_book, name='edit_book'),
    # my_room/1/delete_book/1/
    path('<int:user_id>/delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]