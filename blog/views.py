from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Announcement
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
from django.conf import settings
from .forms import CommentForm
from django.contrib import messages
#from actions.utils import create_action


User = settings.AUTH_USER_MODEL

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/accounts_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

'''class PostsDetailView(DetailView):
    model = Post
'''

def post_detail(request, pk):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
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

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post

    fields = ['title', 'content', 'video', 'img', 'docs']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    success_url = '/'
    fields = ['title', 'content', 'video', 'img', 'docs']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class NoticeListView(ListView):
    model = Announcement
    template_name = 'blog/announcement.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'notices'
    ordering = ['-posted_date']
    paginate_by = 5


'''class NoticeCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    fields = ['title', 'content', 'add_video']

    def form_valid(self, form):
        form.instance.author = self.request.user
        super().form.save()
        return super().form_valid(form)

class NoticeDetailView(DetailView):
    model = Announcement


class NoticeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Announcement
    fields = ['title', 'content', 'add_video']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        notice = self.get_object()
        if self.request.user == notice.author:
            return True
        return False

class NoticeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Announcement
    success_url = '/'
    def test_func(self):
        notice = self.get_object()
        if self.request.user == notice.author:
            return True
        return False
'''
def searchBar(request):
    if request.method == "GET":
        query = request.GET.get('q')
        sub_btn = request.GET.get('submit')

        if query is not None:
            lookups = Q(title__icontains=query)
            results = Post.objects.filter(lookups).distinct()
            context = {
                'results': results,
                'sub_btn': sub_btn,
                'title': 'Search Results'
            }
            return render(request, 'blog/search_posts.html', context)

        else:
            return render(request, 'blog/search_posts.html')
    else:
        return render(request, 'blog/home.html')

def about(request):
    context = {
        'title': "About"
    }
    return render(request, 'blog/about.html', context)

#########################################

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), mimetype="application/force-download")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

