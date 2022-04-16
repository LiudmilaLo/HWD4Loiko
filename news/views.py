from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from .models import *
from .filters import PostFilter
from .forms import PostForm


class AuthorList(ListView):
    model = Author
    context_object_name = 'Authors'
    template_name = 'news/authors.html'


class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news/allnews.html'
    context_object_name = 'Posts'
    paginate_by = 2


class PostSearch(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'news/post_search.html'
    context_object_name = 'Posts'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostCreateView(CreateView):
    template_name = 'news/add.html'
    form_class = PostForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)


class PostUpdateView(UpdateView):
    template_name = 'news/edit.html'
    form_class = PostForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'news/delete.html'
    queryset = Post.objects.all()
    success_url = '/news/news/'


class PostOne(DetailView):
    model = Post
    context_object_name = 'Post'
    queryset = Post.objects.filter()
