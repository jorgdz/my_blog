from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse

class HelloWorld (View):

    def get(self, req):
        data = {
            'name': 'Jorge Diaz Montoya',
            'years': 28,
            'codes': ['Python', 'Django', 'React']
        }

        return render (req, 'hello_world.html', context = data)