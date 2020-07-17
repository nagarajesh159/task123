from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
from django.shortcuts import reverse

from .models import Fruit

# Create your views here.


class CreateFruitView(generic.CreateView):
    model = Fruit
    fields = '__all__'
    success_url = '/fruits/'


class DisplayFruitListView(generic.ListView):
    queryset = Fruit.objects.all()
    context_object_name = 'fruit_list'


def validate_fruit(request):
    name = request.GET.get('name', None)
    data = {
        'is_taken': Fruit.objects.filter(name__iexact=name).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)

