from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


def index(request):
    context = {'title': '首頁', 's': '0'}
    sort_list = TypeInfo.objects.all()
    goods_list = []
    for goods_type in sort_list:
        new_goods = goods_type.goodsinfo_set.order_by('-id')[0:4]
        goods_click = goods_type.goodsinfo_set.order_by('-gclick')[0:3]
        goods_type_name = goods_type.ttitle
        # goods_list.append({'new_goods':new_goods,'goods_click':goods_click,'goods_type_name':goods_type_name})
        goods_list.append([new_goods,goods_click,goods_type_name])
    context['dict'] = goods_list
    return render(request, 'goods/index.html', context)


def list_goods(request, ptype, pindex, sort_condition):
    context = {'title': '水果', 'id': '1'}        # 用初始化於模板的參數

    if int(ptype) < 1:                           # 用於判斷類型
        ptype = 1
    elif int(ptype) > 6:
        ptype = 6

    goods_type = TypeInfo.objects.filter(isDelete=False,pk=ptype)[0]    # 獲取所有水果的列表
    if sort_condition == '':
        goods_list = goods_type.goodsinfo_set.all()
    elif sort_condition == '_sort_price':
        goods_list = goods_type.goodsinfo_set.order_by('gprice')
    elif sort_condition == '_click':
        goods_list = goods_type.goodsinfo_set.order_by('gclick')
    new_goods_list = goods_type.goodsinfo_set.order_by('-id')[0:2]
    p = Paginator(goods_list, 1)                                       # 進行分頁， 每頁15個商品

    if int(pindex) < 1:
        pindex = 1

    elif int(pindex) > p.num_pages:
        pindex = p.num_pages

    page_goods_list = p.page(int(pindex))                               # 獲取該頁的商品列表
    page_list = []
    if int(pindex) < 4 :
        for i in range(1, int(pindex)+1):
            page_list.append(str(i))
        if int(pindex) + 2 >= p.num_pages:
            for j in range(int(pindex)+1,p.num_pages+1):
                page_list.append(str(j))
        else:
            page_list.extend([str(int(pindex)+1), str(int(pindex)+2), '...'])
    elif (int(pindex) >= 4) and (int(pindex) + 2 < p.num_pages):
        page_list.append('...')
        for i in range(int(pindex)-2, int(pindex)+3):
            page_list.append(str(i))
        page_list.append('...')
    else:
        page_list.append('...')
        for i in range(int(pindex) - 2, p.num_pages + 1):
            page_list.append(str(i))

    context['page_list'] = page_list
    context['goods_list'] = page_goods_list
    context['goods_type'] = goods_type
    context['new_goods_list'] = new_goods_list
    return render(request, 'goods/list.html', context)


def goods_detail(request, goods_type_id, goods_id):

    """
    request: Http請求
    goods_type_id: 商品類型的id
    goods_id: 商品名的id
    return: 查詢商品id爲goods_id的詳細頁
    """

    context = {'title': '詳細頁'}

    try:    #判斷是否有此類商品，沒有就返回404頁面
        goods_type = TypeInfo.objects.get(id=goods_type_id)
    except:
        return render(request, '404.html')

    try:    #判斷是否有此商品，沒有就返回404頁面
        goods = goods_type.goodsinfo_set.get(id=goods_id)
    except:
        return render(request, '404.html')

    new_goods_list = goods_type.goodsinfo_set.order_by('-id')[0:2]

    context['goods'] = goods
    context['goods_type'] = goods_type
    context['new_goods_list'] = new_goods_list

    return render(request, 'goods/detail.html', context)

