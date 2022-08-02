"""Post views"""

#Utilities Python
from datetime import datetime

#Django
from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.

posts = [
    {
        'title': 'La vitta deio Colione',
        'user': {
            'name': 'Mariana Torres',
            'picture': 'https://picsum.photos/60/60?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200?image=1036',
    },
    {
        'title': 'Grasberry Framboises',
        'user': {
            'name': 'Ismael Mancinni',
            'picture': 'https://picsum.photos/60/60?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200?image=102',
    },
    {
        'title': 'Puma',
        'user': {
            'name': 'Roque Batello',
            'picture': 'https://picsum.photos/60/60?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200?image=1074',
    },
]



def list_posts(request):
    """List eknowed posts"""
    return render(request, 'feed.html', {'posts': posts})