from django.urls import path,include
from . import views
from .views import QuestionListView,QuestionDetailView,QuestionCreateView,QuestionUpdateView,get_answer,answer,AnswerListView,upvote,downvote
urlpatterns = [
    path('', QuestionListView.as_view(), name='BITS_Assist-question'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='questions-detail'),
    path('questions/new/', QuestionCreateView.as_view(), name='questions-create'),
    path('questions/<int:pk>/update', QuestionUpdateView.as_view(), name='questions-update'),
    path('answer/<int:pk>/',answer, name='BITS_Assist-answer'),
    path('<int:pk>/answer/',AnswerListView.as_view(),name = 'ANSWERS'),
    path('questions/<int:pk>/upvote',upvote,name = 'like'),
    path('questions/<int:pk>/downvote',downvote,name = 'dislike'),
]
