from django.shortcuts import render, redirect, get_object_or_404
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, ListView
from django.db.models import Count
from django.utils import timezone
from .models import Board, Topic, Post
from .forms import NewTopicForm, PostForm

# Create your views here.

# def home(request):
#     boards = Board.objects.all()
#     return render(request, 'boards/home.html', {'boards':boards})

class BoardListView(ListView):
    """ 视图 `home` 的重构，改为类视图 """
    model = Board
    template_name = 'boards/home.html'
    context_object_name = 'boards'

# def board_topics(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     queryset = board.topics.order_by('-last_update').annotate(replies=Count('posts') - 1)
#     page = request.GET.get('page', 1)
#     paginator = Paginator(queryset, 20)
#     try:
#         topics = paginator.page(page)
#     except PageNotAnInteger:
#         topics = paginator.page(1)
#     except EmptyPage:
#         topics = paginator.page(paginator.num_pages)
#     return render(request, 'boards/topics.html', {'board':board, 'topics':topics})

class TopicListView(ListView):
    """ 视图 board_topics的重构，改为类视图 """
    model = Topic
    context_object_name = 'topics'
    template_name = 'boards/topics.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        kwargs['board'] = self.board
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.board = get_object_or_404(Board, pk=self.kwargs.get('pk'))
        queryset = self.board.topics.order_by('-last_update').annotate(replies=Count('posts') - 1)
        return queryset

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

# def topic_posts(request, pk, topic_pk):
#     topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
#     topic.views += 1
#     topic.save()
#     posts = Post.objects.filter(topic_id=topic_pk)
#     return render(request, 'boards/topic_posts.html', {'topic':topic, 'posts':posts})

class PostListView(ListView):
    """ 视图 topic_posts 的重构，改为类视图"""
    model = Post
    context_object_name = 'posts'
    template_name = 'boards/topic_posts.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        session_key = 'viewed_topic_{}'.format(self.topic.pk)
        # 相同的用户再次刷新页面的时候只统计一次
        if not self.request.session.get(session_key, False):
            self.topic.views += 1
            self.topic.save()
            self.request.session[session_key] = True
        kwargs['topic'] = self.topic
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.topic = get_object_or_404(Topic, board__pk=self.kwargs.get('pk'), pk=self.kwargs.get('topic_pk'))
        queryset = self.topic.posts.order_by('created_at')
        return queryset

@login_required
def reply_topic(request, pk, topic_pk):
    print("0S")
    print("pk:"+str(pk))
    print("topic_pk"+str(topic_pk))
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    posts = Post.objects.filter(topic_id=topic_pk)
    if request.method == 'POST':
        print("1S")
        form = PostForm(request.POST)
        if form.is_valid():
            print("4S")
            post = form.save(commit=False)
            print("message21:"+post.message)
            post.topic = topic
            post.created_by = request.user
            post.save()

            topic.last_update = timezone.now()
            topic.save()
            

            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        print("3S")
        form =PostForm()
    return render(request, 'boards/reply_topic.html', {'topic': topic, 'posts': posts, 'form': form})

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    fields = ('message',)
    template_name = 'boards/edit_post.html'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post .updated_at = timezone.now()
        post.save()
        return redirect('topic_posts', pk=post.topic.board.pk, topic_pk=post.topic.pk)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)