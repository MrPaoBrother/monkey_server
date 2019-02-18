# -*- coding:utf8 -*-

from django.db import models

"""
class BchBlockList(models.Model):
    class Meta:
        db_table = 'bch_block_list'
    id = models.IntegerField(primary_key=True, auto_created=True)
    hash = models.CharField(max_length=100, default="")
    txlength = models.CharField(max_length=100, default="")
    height = models.CharField(max_length=100, default="")
    time = models.CharField(max_length=100, default="")
    size = models.CharField(max_length=100, default="")
    poolInfo = models.CharField(max_length=255, default="")
    create_time = models.DateTimeField(auto_now=True)
    modify_time = models.DateTimeField(auto_now=True)
    extra = models.CharField(max_length=100, default="")


class BlockRelateList(models.Model):
    class Meta:
        db_table = 'block_relate_list'

    id = models.IntegerField(primary_key=True, auto_created=True)
    height = models.IntegerField(default=0)
    input_addrs = models.TextField(default="")
    output_addrs = models.CharField(default="")
    txid = models.CharField(max_length=100, default="")
    txid_index = models.CharField(max_length=50, default=0)
    is_head = models.IntegerField(default=0)  # 默认不是头结点
    create_time = models.DateTimeField(auto_now=True)
    extra = models.CharField(max_length=255, default="")


class BlockDataDeal(models.Model):
    class Meta:
        db_table = 'block_data_deal'
    id = models.IntegerField(primary_key=True, auto_created=True)
    height = models.IntegerField(primary_key=True, default=0)
    tx_nums = models.IntegerField(default=0)
    addr = models.CharField(max_length=50, default="")
    input_nums = models.IntegerField(default=0)
    output_nums = models.IntegerField(default=0)
    input_fees = models.CharField(max_length=10, default="")
    output_fees = models.CharField(max_length=10, default="")
    block_time = models.CharField(max_length=10, default="")
"""


class TxsRelated(models.Model):
    class Meta:
        """
        交易关系表
        """
        db_table = 'txs_related'
    id = models.BigIntegerField(primary_key=True, auto_created=True)
    tx_hid = models.BigIntegerField(max_length=20)
    addr = models.CharField(max_length=100)
    position = models.IntegerField(max_length=4)
    tx_index = models.BigIntegerField(max_length=20)
    related_tx_index = models.BigIntegerField(max_length=20, default=0)
    addr_value = models.BigIntegerField(max_length=20, default=0)
    create_time = models.DateTimeField(auto_now=True)


class PicDetail(models.Model):
    class Meta:
        db_table = 'pic_detail'
    id = models.IntegerField(primary_key=True, auto_created=True)
    pic_name = models.CharField(max_length=255, default="")
    pic_url = models.CharField(max_length=300, default="")
    pic_type = models.IntegerField(default=0)
    pic_description = models.CharField(max_length=300, default="")
    create_time = models.DateTimeField(auto_now=True)
    modify_time = models.DateTimeField(auto_now=True)


class MonkeyRecord(models.Model):
    class Meta:
        db_table = 'monkey_record'
    id = models.IntegerField(primary_key=True, auto_created=True)
    address = models.CharField(max_length=255, default="")
    randombackground = models.IntegerField(max_length=5, default=1)
    randomanimals = models.IntegerField(max_length=5, default=0)
    # 猴子穿戴或者没有穿戴的样子
    state = models.IntegerField(max_length=5, default=0)
    go_home_time = models.BigIntegerField(max_length=10, default="")
    description = models.CharField(max_length=300, default="")
    # 默认在家
    is_home = models.IntegerField(default=1)
