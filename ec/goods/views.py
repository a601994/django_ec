from django.shortcuts import render


def index(request):
    context = {'title': '首頁', 's': '0'}
    return render(request, 'goods/index.html', context)

def fruit(request):
    context = {'title': '水果', 'id': '1'}
    return render(request, 'goods/list.html', context)