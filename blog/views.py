from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def search_view(request):
    pass


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # descending order ...
    paginate_by = 5 # adding pagination function to the home/index view...(5 posts at a time)


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
#


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'category', 'content', 'post_image']

    def form_valid(self, form): # overiding the form_valid method to track the present Logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'category', 'content', 'post_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # A test function that confirms the right owner of a particular post....
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):  # A test function that confirms that the right owner is the one deleting a post..
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# other links in function based views..

def faq_view(request):
    template_name = 'blog/faq.html'
    return render(request, template_name)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


# A code to be added to the settings/views for message/bootstrap buttons to work very well. ..
    # from django.contrib.messages import constants as messages
#
# MESSAGE_TAGS = {
#     messages.DEBUG: 'alert-info',
#     messages.INFO: 'alert-info',
#     messages.SUCCESS: 'alert-success',
#     messages.WARNING: 'alert-warning',
#     messages.ERROR: 'alert-danger',
# }


# A detail view that follows the django convention method of structure..
#     # using the object as the context variable passed. ..

# re-writing the detailview

# def postDetail_view(request, pk):
#     object = get_object_or_404(Post, pk=pk)
#     template_name = 'blog/post_detail.html'
#     # adding the forms here ...
#     # realising that the owner will be the only one to comment here...
#     context ={
#         'object': object
#     }
#     return render(request, template_name, context)