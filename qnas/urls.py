from django.urls import path 
from . import views 

app_name = 'qnas'
urlpatterns = [
    # qna/
    path('', views.QnaListView.as_view(), name='qna_list'),
    # qna/1/detail/
    path('<int:qna_id>/detail/', views.qna_detail, name='qna_detail'),
    # qna/answer_delete/1/ 
    path('<int:qna_id>/answer_delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    # qna/create/
    path('create/', views.qna_create, name='qna_create'),
    # qna/1/update/
    path('<int:qna_id>/update/', views.qna_update, name='qna_update'),
    # qna/1/delete/
    path('<int:qna_id>/delete/', views.qna_delete, name='qna_delete'),
]