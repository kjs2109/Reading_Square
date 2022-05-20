from django.urls import path 
from . import views 

app_name = 'qnas'
urlpatterns = [
    # qna/
    path('', views.QnaListView.as_view(), name='qna_create'),
    # qna/1/detail/

    # qna/create/

    # qna/1/update/

    # qna/1/delte/

]