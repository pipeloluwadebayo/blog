from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout





# Create your views here.


class Index(ListView):
    model = Post
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Index, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticleView(DetailView):
    model = Post
    template_name = 'articles.html'

    

class NewPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'newpost.html'



class UpdatePost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('index')

def CategoryView(request, categorys):
    category_posts = Post.objects.filter(category=categorys.replace('-', ' '))
    return render(request, 'category.html', {'categorys': categorys.title().replace('-', ' '), 'category_posts' : category_posts})

def get_context_data(self, *args, **kwargs):
    cat_menu = Category.objects.all()
    context = super(CategoryView, self).get_get_context_data(*args, **kwargs)        
    context["cat_menu"] = cat_menu
    return context


class CommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('index')



class UserLogin(LoginView):
    template_name = 'login.html'


def logout_request(request):
	logout(request)
	return redirect("index")