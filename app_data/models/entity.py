# -*- coding:utf8 -*-

from django.db import models


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


class TravelPlayer(models.Model):
    class Meta:
        db_table = 'travel_player'
    id = models.IntegerField(primary_key=True, auto_created=True)
    uid = models.BigIntegerField(default=0)
    addr = models.CharField(max_length=255)
    player_key = models.IntegerField(max_length=10)
    player_level = models.IntegerField(max_length=4, default=0)
    player_power = models.IntegerField(max_length=6)
    logintime = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now=True)
    modify_time = models.DateTimeField(auto_now=True)
    has_monkey = models.IntegerField(max_length=4, default=0)


class TravelLevel(models.Model):
    class Meta:
        db_table = 'travel_level'
    id = models.IntegerField(primary_key=True, auto_created=True)
    level_key = models.IntegerField(default=0)
    level_difficulty = models.IntegerField()
    is_special = models.IntegerField()
    special_count = models.IntegerField()
    all_count = models.IntegerField()
    add_range = models.IntegerField()
    add_min = models.IntegerField()
    level_status = models.IntegerField()
    description = models.CharField(max_length=1000, default="")


class TravelMonkey(models.Model):
    class Meta:
        db_table = 'travel_monkey'
    id = models.IntegerField(primary_key=True, auto_created=True)
    uid = models.BigIntegerField(default=0)
    mon_key = models.IntegerField()
    mon_fight = models.IntegerField()
    mon_state = models.IntegerField()
    mon_level = models.IntegerField()
    mon_value = models.BigIntegerField(default=0)
