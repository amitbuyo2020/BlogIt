from django.urls import path
from . import views
from .views import (PostListView, PostCreateView,
                    PostUpdateView, PostDeleteView, UserPostListView,
                    )


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='new-post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:email>', UserPostListView.as_view(), name='user-posts'),
    path('search/', views.searchBar, name='searchBar'),

]


'''urlpatterns = [
    path('', PostListView.as_view(), name='article-home'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post-article'),
    #path('search/', views.searchBar, name='searchBar'),
    path('announcements/', NoticeListView.as_view(), name='announcements'),
    path('article/new/', ArticleCreateView.as_view(template_name='blog/article_form.html'), name='new-article'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update')
]
'''
