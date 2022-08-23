"""Post views"""

#Utilities Python
from datetime import datetime

#Django
# from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView 


# Forms
from posts.forms import PostForm 

# Models
from posts.models import Post


# Create your views here.

# posts = [
#     {
#         'title': 'La vitta deio Colione',
#         'user': {
#             'name': 'Mariana Torres',
#             'picture': 'https://picsum.photos/60/60?image=1027'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/200/200?image=1036',
#     },
#     {
#         'title': 'Grasberry Framboises',
#         'user': {
#             'name': 'Ismael Mancinni',
#             'picture': 'https://picsum.photos/60/60?image=1005'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/200/200?image=102',
#     },
#     {
#         'title': 'Puma',
#         'user': {
#             'name': 'Roque Batello',
#             'picture': 'https://picsum.photos/60/60?image=883'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/200/200?image=1074',
#     },
# ]



class PostsFeedView(LoginRequiredMixin, ListView):
    """ Return all published posts """

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 9
    context_object_name = 'posts'



# posts = Post.objects.all().order_by('-created')
# @login_required
# def list_posts(request):
#     """List eknowed posts"""
#     return render(request, 'posts/feed.html', {'posts': posts})


class PostDetailView(LoginRequiredMixin, DetailView):
    """ The detail of JUST ONE Post """

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'



class PostCreateView(LoginRequiredMixin, CreateView):
    """ Create a New post. """

    template_name =  'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """ Add user and profile to context """
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
        



# @login_required
# def create_post(request):
#     """ Create new post view"""
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('posts:feed')
#     else:
#         form = PostForm()

#     return render(
#         request=request,
#         template_name='posts/new.html',
#         context={
#             'form': form,
#             'user': request.user,
#             'profile': request.user.profile
#         }
#     )

