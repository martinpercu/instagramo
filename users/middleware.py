"""
Middleware EXPERIMENT
Force user to have biography and profile picture
"""

# Django
from django.shortcuts import render, redirect
from django.urls import reverse


class ProfileFullDataCompletMiddleware:
    """ 
    Force user to have biography and profile picture

    Force user to have a biography and profle picture in order to user the app

    Is user doesn' have redirect to update profile in order to add a picture and a biography
    """

    def __init__(self, get_response):
        """middleware start here"""
        self.get_response = get_response

    def __call__(self, request):
        """ Code to execute before the view is called"""
        if not request.user.is_anonymous:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                if request.path not in [reverse('update_profile'), reverse('logout') ]:
                    return redirect('update_profile')

        response = self.get_response(request)

        return response