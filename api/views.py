from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.


def index(request):
    return HttpResponse('success')


class SignUpView(CreateView):
    template_name = 'api/signup.html'
    form_class = UserCreationForm
    success_url = '/api/'


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)

