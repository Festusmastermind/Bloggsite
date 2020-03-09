from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# including categories and images to the posts

class Post(models.Model):
    title = models.CharField(max_length=100)
    category_choice = (
        ('Education', 'Education'),
        ('Fashion', 'Fashion'),
        ('Arts', 'Arts'),
        ('Politics', 'Politics'),
        ('Sports', 'Sports'),
        ('Graphics', 'Graphics'),
        ('Programming', 'Programming'),
        ('Technologies', 'Technologies'),
        ('Entertainment', 'Entertainment'),
        ('Animation', 'Animation'),
        ('Business', 'Business'),
        ('others', 'others')
    )
    category = models.CharField(max_length=50, choices=category_choice)
    content = models.TextField()
    post_image = models.ImageField(upload_to='post_pics', null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# including a comment system

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment by {self.name}'

        # email = models.EmailField()
        # active = models.BooleanField(default=False)