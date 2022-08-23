""" POSTS ADMIN """

#Django
from django.contrib import admin


#Models
from posts.models import Post

# Register your models here.


class PostAdmin(Post):
    """ Post in admin """
    list_display = ('id', 'user', 'profile', 'title', 'photo', 'created')

    list_filter = ['created', 'modified',]


admin.site.register(Post)
