from django.shortcuts import render


def index(request):
    context = {'title': 'Главная'}
    response = render(request, 'main/index.html', context)
    return response
