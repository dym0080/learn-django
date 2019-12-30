from django.urls import path

from . import views

# app_name = 'boards'
urlpatterns =[
    path('', views.home, name='home'),
    path('<int:pk>/', views.board_topics, name='board_topics'),
    path('<int:pk>/new/', views.new_topic, name='new_topic'),
    path('<int:pk>/topics/<int:topic_pk>/', views.topic_posts, name='topic_posts'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
]