from django import forms
from blog.models import Comment



# creating the comment form

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'name']


        def clean(selfs):
            # extra validation will be passed here later if not by a pre-signal...
            pass