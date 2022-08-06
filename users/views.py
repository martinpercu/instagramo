""" This is the users view"""

#Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required  #nor really needed because is not possible to arrive the view if you are not already logged
# Create your views here.


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
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'The username and/or password not found'})
    return render(request, 'users/login.html')

@login_required #in normal use no need this decorator.---> You are in this 'post' page if you are already logged.
def logout_view(request):
    """ Logout view """

    logout(request)

    return render(request, 'users/login.html', {'messageLogout': 'You just logout.'})