"""instagramoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Django
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

# from instagramoapp import views as local_views
# from posts import views as posts_views
# from users import views as users_views

# for heroku ???
# from django.views.static import serve
# from django.conf.urls import url


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include(('posts.url', 'posts'), namespace='posts')),

# The paths "commented" down are now in the folder "post" in the file "url.py"
    # path('', posts_views.list_posts, name='feed'),
    # path('posts/new/', posts_views.create_post, name='create_post'),


    path('user/', include(('users.url', 'users'), namespace='users')),

# The paths "commented" down are now in the folder "post" in the file "url.py"
    # path('users/login/', users_views.login_view, name='login'),
    # path('users/logout/', users_views.logout_view, name='logout'),
    # path('users/signup/', users_views.signup, name='signup'),
    # path('users/me/profile/', users_views.update_profile, name='update_profile')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
