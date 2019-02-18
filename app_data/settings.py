# -*- coding:utf8 -*-
import os
SECRET_KEY = '5n_=nvbtprsei+93l1im%)+4skc4*x37va_3xi0p75_e3b4rxt'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INSTALLED_APPS = [
    'app_data'
]

DATABASES = {
    'bitrun': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bitrun',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '123.207.75.151',
        'PORT': 3306,
        'OPTIONS': {'autocommit': True, }
    }
}
DATABASES['default'] = DATABASES['bitrun']

DEBUG = True


class DBRouter(object):

    tables = (
        'pic_detail',
        'monkey_record',
        'travel_level',
        'travel_monkey',
        'travel_player'
    )

    def db_for_read(self, model, **hints):
        db = None
        tbl = model._meta.db_table
        if tbl in self.tables:
            db = 'bitrun'
        return db

    def db_for_write(self, model, **hints):
        db = None
        tbl = model._meta.db_table
        if tbl in self.tables:
            db = 'bitrun'
        return db
DATABASE_ROUTERS = ['app_data.settings.DBRouter', ]

TIME_ZONE = 'Asia/Shanghai'

USE_TZ = False
