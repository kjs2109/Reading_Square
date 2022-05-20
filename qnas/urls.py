from django.urls import path 
from . import views 

app_name = 'qnas'
urlpatterns = [
    # qna/
    path('', views.QnaListView.as_view(), name='qna_list'),
    # qna/1/detail/
    path('<int:qna_id>/detail/', views.qna_detail, name='qna_detail'),
    # qna/create/

    # qna/1/update/

    # qna/1/delte/

]