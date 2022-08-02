"""Post views"""

#Utilities Python
from datetime import datetime

#Django
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

posts = [
    {
        'name': 'La vitta deio Colione',
        'user': 'Marianito Torres',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200?image=1036',
    },
    {
        'name': 'Grasberry Framboises',
        'user': 'Raquel Mancinni',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200?image=102',
    },
    {
        'name': 'Puma',
        'user': 'Roque Batello',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200?image=1074',
    },
]



def list_posts(request):
    """List eknowed posts"""
    content = []
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user} - <i>{timestamp}</i></small></p>
        <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))