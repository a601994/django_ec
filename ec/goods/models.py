from django.db import models


class Fruit(models.Model):
    name = models.CharField(max_length=20)                              # 商品名
    price = models.FloatField()                                         # 商品價格
    brief = models.CharField(max_length=100)                            # 商品簡介
    detail = models.CharField(max_length=500)                           # 商品詳情
    sold = models.IntegerField(default=0)                               # 商品的銷量（重量）
    origin = models.CharField(max_length=50, default='暫無評價')          # 商品的圖片地址
    is_delete = models.BooleanField(default=False)                      # 刪除產品