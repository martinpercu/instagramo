"""
Users URLs
"""

# Django
from django.urls import path
from django.views.generic import TemplateView

# Views
from users import views



urlpatterns = [


    # Management
    path(
        route='users/login/',
        # view= views.login_view, 
        view= views.LoginView.as_view(), 
        name='login'
    ),
    path(
        route='users/logout/',
        # view= views.logout_view, 
        view= views.LogoutView.as_view(), 
        name='logout'
    ),
    path(
        route='users/signup/',
        # view= views.signup,
        view= views.SignUpView.as_view(),
        name='signup'
    ),
    path(
        route='users/me/profile/',
        # view= views.update_profile,
        view= views.UpdateProfileView.as_view(),
        name='update_profile'
    ),


    # Posts
    path(
        route='<str:username>/',
        # view=TemplateView.as_view(template_name='users/detail.html'),
        view=views.UserDetailView.as_view(),
        name='detail'
    )


]