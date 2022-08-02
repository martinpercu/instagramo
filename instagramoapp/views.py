"""This is the Intagramo views"""

#Utilities - Python
from datetime import datetime
import json

#Django
from django.http import HttpResponse




def hello_world(request):
    """Return something just for fun"""
    return HttpResponse('Bonjour les amis. L\'heure actual est: {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def debugger_console(request):
    """
    this stop and open a debugger console. We can use to see what there are in 
    the parameters. In this case "request
    """
    import pdb
    pdb.set_trace()
    return HttpResponse('HI This had openned the console debugger. Already close by yourself')


def sorted_numbers(request):
    """
    Adding in the url this ===>  /?numbers=40,25,12,5,50,80
    Return a json whit the numbers in order
    """
    numbers = request.GET['numbers'].split(',')
    numbers = [int(i) for i in numbers]
    numbers = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': numbers,
        'message': "Integers in order"
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application.json'
        )

    
def say_hi(request, name, age):
    """Retur something.. in the url ===>  /Mariano/34"""
    if age < 18:
        message = 'Sorry {}, you are to young to see this content'.format(name)
    else:
        message = 'Hello {}. Welcome to you place'.format(name)

    return HttpResponse(str(message))

