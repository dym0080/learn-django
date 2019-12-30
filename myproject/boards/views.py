from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Board, Topic, Post
from .forms import NewTopicForm

# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request, 'boards/home.html', {'boards':boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    topics = Topic.objects.filter(board_id=pk)
    return render(request, 'boards/topics.html', {'board':board, 'topics':topics})

@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        user = request.user
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()

            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'boards/new_topic.html', {'board':board, 'form':form})

def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    posts = Post.objects.filter(topic_id=topic_pk)
    print(11)
    print(posts)
    print(12)
    return render(request, 'boards/topic_posts.html', {'topic':topic, 'posts':posts})