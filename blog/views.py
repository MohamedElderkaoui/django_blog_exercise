from django.shortcuts import get_object_or_404, render
from django.views import generic

from .forms import CommentForm
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3

class UserPostList(LoginRequiredMixin,  generic.ListView):
    '''Muestra los posts de un usuario en particular'''
    model = Post
    template_name = "user_posts.html"
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by("-created_on")


def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )
