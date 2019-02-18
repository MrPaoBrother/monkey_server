# -*- coding:utf8 -*-
import logging
import os
import settings
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'app_data.settings'
django.setup()
logging.basicConfig(filename="../../log/%s.log" % settings.psm, level=logging.INFO)
from app_data.models.entity import PicDetail


def upload_img(local_path, upload_name, bucket_name=settings.bucket_name, ttl=7200):
    """
    上传图片到七牛云
    :param local_path: 本地文件路径
    :param upload_name: 上传文件名
    :param bucket_name: 七牛申请的存储空间名称
    :param ttl: 过期时间
    :return: 返回图片地址
    """
    from qiniu import Auth, put_file
    import re
    q = Auth(access_key=settings.AccessKey, secret_key=settings.SecretKey)
    token = q.upload_token(bucket_name, upload_name, ttl)
    ret, info = put_file(token, upload_name, local_path)
    pat_status = 'status_code:(.*?),'
    status_code = re.compile(pat_status, re.S).findall(str(info))
    if len(status_code) > 0:
        if int(status_code[0]) == 200:
            return settings.qiniu_domain + upload_name
    return "failed upload img failed"


def save_image():
    with open('./images/imags.json', 'rb') as fs:
        data = ''.join(fs.readlines())
        import json
        data = json.loads(data)
    for img_name, description in data.items():
        try:
            tos_url = upload_img("./images/%s"%img_name, img_name, bucket_name=settings.bucket_name, ttl=7200)
            PicDetail.objects.update_or_create(pic_name=img_name, defaults=dict(pic_url=tos_url, pic_type=0,
                                                                                pic_description=description))
            print "upload image_name:%s success" % img_name
        except Exception as e:
            print e
    """
    image_names = os.listdir(r'./images')
    for image_name in image_names:
        try:
            tos_url = upload_img("./images/%s"%image_name, image_name, bucket_name=settings.bucket_name, ttl=7200)
            PicDetail.objects.update_or_create(pic_name=image_name, defaults=dict(pic_url=tos_url, pic_type=0))
            print "upload image_name:%s success" % image_name
        except Exception as e:
            print e
    """


def save_image1():
    image_names = os.listdir(r'./computer_images')
    for image_name in image_names:
        try:
            tos_url = upload_img("./computer_images/%s" % image_name, image_name, bucket_name=settings.bucket_name, ttl=7200)
            PicDetail.objects.update_or_create(pic_name=image_name, defaults=dict(pic_url=tos_url, pic_type=0))
            print "upload image_name:%s success" % image_name
        except Exception as e:
            print e


if __name__ == "__main__":
    """
    tos_url = upload_img('./images/1-0-1.jpg', '1-0-1.jpg', bucket_name=settings.bucket_name, ttl=7200)
    print tos_url
    """
    save_image1()
