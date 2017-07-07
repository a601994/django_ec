from django.shortcuts import render
from .models import Fruit
from django.core.paginator import Paginator


def index(request):
    context = {'title': '首頁', 's': '0'}
    return render(request, 'goods/index.html', context)


def fruit(request, pindex):
    context = {'title': '水果', 'id': '1'}               # 用初始化於模板的參數
    fruit_list = Fruit.objects.filter(is_delete=False)  # 獲取所有水果的列表
    p = Paginator(fruit_list, 15)                       # 進行分頁， 每頁15個商品
    if pindex == '':                                    # 如果沒有寫頁碼，
        pindex = '1'                                    # 賦值爲1

    page_fruit_list = p.page(int(pindex))               # 獲取該頁的商品列表
    page_list = p.page_range                            # 得到頁碼列表
    count = p.count                                     # 得到頁碼總數

    context['fruit_list'] = page_fruit_list
    context['page_list'] = page_list
    context['pindex'] = pindex
    context['count'] = count
    return render(request, 'goods/list.html', context)


def sort_price_fruit(request, pindex):
    context = {'title': '水果', 'id': '1'}  # 用初始化於模板的參數
    fruit_list = Fruit.objects.filter(is_delete=False).order_by('price')  # 獲取所有水果的列表
    p = Paginator(fruit_list, 15)  # 進行分頁， 每頁15個商品
    if pindex == '':  # 如果沒有寫頁碼，
        pindex = '1'  # 賦值爲1

    page_fruit_list = p.page(int(pindex))  # 獲取該頁的商品列表
    page_list = p.page_range  # 得到頁碼列表
    count = p.count  # 得到頁碼總數

    context['fruit_list'] = page_fruit_list
    context['page_list'] = page_list
    context['pindex'] = pindex
    context['count'] = count
    return render(request, 'goods/list.html', context)


def fruit_detail(request, goods_id):
    item = Fruit.objects.filter(id=goods_id)[0] #獲取相應的商品
    context = {'title': item.name}              # 模板初始化
    context['item'] = item

    return render(request, 'goods/detail.html', context)