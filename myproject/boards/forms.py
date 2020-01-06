from django import forms
from .models import Topic, Post

# Django 使用两种类型的 form：forms.Form 和 forms.ModelForm。
# Form 类是通用的表单实现。我们可以使用它来处理与应用程序 model 没有直接关联的数据。
# ModelForm 是 Form 的子类，它与 model 类相关联。

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'row':5, 'placeholder':'Input your message.'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message',]