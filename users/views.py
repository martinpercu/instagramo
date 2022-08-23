""" This is the users view"""

# Create your views here.


# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required  #nor really needed because is not possible to arrive the view if you are not already logged
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse , reverse_lazy

# Models
from django.contrib.auth.models import User
from posts.models import Post


# Forms
# from users.forms import ProfileForm
from users.forms import SignupForm
from users.models import Profile


class UserDetailView(LoginRequiredMixin, DetailView):
    """ User Detail View """

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """ Add user's posts for the context """
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context



# def for an experimental django Middleware.... 

# @login_required
# def update_profile(request):
#     """ 
#     Update user profile .. atention!! experiment to use Middlewares    
#     """
#     profile = request.user.profile

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.cleaned_data

#             profile.website = data['website']
#             profile.biography = data['biography']
#             profile.phone_number = data['phone_number']
#             profile.picture = data['picture']

#             profile.save()
#             print(form.cleaned_data)

#             # url = reverse('users:feed')

#             url = reverse('users:detail', kwargs={'username': request.user.username})
#             return redirect(url)
#     else:
#         form = ProfileForm()


#     return render(
#         request = request,
#         template_name = 'users/update_profile.html',
#         context = {
#             'profile': profile,
#             'user': request.user,
#             'form': form
#         }
#     )



class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """ Update Profile View for users """

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """ return user profile """
        return self.request.user.profile

    def get_success_url(self):
        """ return to users profile """
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username':username})
    



def login_view(request):
    """ Login view """

    # import pdb; pdb.set_trace()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # We check in console if POST is working OK
        # print(username, password)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'The username and/or password not found'})
    return render(request, 'users/login.html')

@login_required #in normal use no need this decorator.---> You are in this 'post' page if you are already logged.
def logout_view(request):
    """ Logout view """

    logout(request)

    return render(request, 'users/login.html', {'messageLogout': 'You just logout.'})


# def signup(request):
#     """Signup View"""
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users:login')
#     else:
#         form = SignupForm()
#     return render(
#         request=request,
#         template_name='users/signup.html',
#         context={'form': form}
#     )
        

class SignUpView(FormView):
    """ Signup View """

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """ Save form info in DB ---> Save new user """
        form.save()

        
        return super().form_valid(form) 

 