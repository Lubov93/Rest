from django.conf.urls import url
from  posts.views import *
from django.urls import path

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
    url(r'^choices/', ChoiceList.as_view(), name="choice_list"),
    url(r'^vote/', CreateVote.as_view(), name="create_vote"),
    path('post/<int:pk>/', CommentDetail.as_view()),

]