from django.urls import path
from . import views
from .views import Index, ArticleView, NewPost, UpdatePost, DeletePost, CategoryView, UserLogin, CommentView



urlpatterns=[
    path('',Index.as_view(), name='index'),
    path('post/<int:pk>', ArticleView.as_view(), name='articles'),
    path('newpost/', NewPost.as_view(), name='newpost'),
    path('post/edit/<str:pk>', UpdatePost.as_view(), name='update'),
    path('post/<int:pk>/delete', DeletePost.as_view(), name='delete'),
    path('category/<str:categorys>/', CategoryView, name='category'),
    path('login/', UserLogin.as_view(), name='login'),
    path("logout", views.logout_request, name= "logout"),
    path('post/<int:pk>/comment', CommentView.as_view(), name='comments')
]
