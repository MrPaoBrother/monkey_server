# -*- coding:utf8 -*-
import threading, time, datetime, random

import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'app_data.settings'
django.setup()

from app_data.models.entity import PicDetail, MonkeyRecord

base_domain = "https://yimixiaoyuan.top/"
random_activities = [u"正在玩呢", u"快回来了", u"认识了新朋友，在他家吃饭"]


class ApiProcess(object):
    def __init__(self):
        #threading.Thread(target=playing).start()
        pass

    def get_goods(self):
        result = []
        good_indexes = [2, 4, 8, 16, 32]
        for good in good_indexes:
            real_path = base_domain + "%d.jpg" % good
            result.append(real_path)
        return result

    def get_images(self, image_names):
        import random
        image_urls = []
        image_list = ["https://yimixiaoyuan.top/random1.jpg",
              "https://yimixiaoyuan.top/random2.jpg",
              "https://yimixiaoyuan.top/random3.jpg",
              "https://yimixiaoyuan.top/random4.jpg",
              "https://yimixiaoyuan.top/random5.jpg"]
        image_names = image_names.split(',')

        for image_name in image_names:
            image_name = image_name.split('-')
            image_name[-1] = "0"
            image_name = "-".join(image_name)
            remote_image_name = "https://yimixiaoyuan.top/" + image_name + ".jpg"
            image_urls.append(remote_image_name)
            #pic_obj = PicDetail.objects.filter(pic_name__contains=image_name).first()
            #if not pic_obj:
              #  random_image = random.choice(image_list)
                #image_urls.append(random_image)
                #image_list.remove(random_image)
                #if not image_list:
                  #  image_list = ["https://yimixiaoyuan.top/random1.jpg",
               #"https://yimixiaoyuan.top/random2.jpg",
               #"https://yimixiaoyuan.top/random3.jpg",
               #"https://yimixiaoyuan.top/random4.jpg",
               #"https://yimixiaoyuan.top/random5.jpg"]
                #continue
            #image_urls.append(pic_obj.pic_url)
        return image_urls

    def get_image_by_type(self, image_type):
        import random
        if str(image_type) == '1':
            # 电脑 1,2,3
            img_index = int(random.random() * 3 + 1)
            return base_domain + "image_computer%d.jpg" % img_index
        if str(image_type) == '2':
            # 床 4,5,6
            img_index = int(random.random() * 3 + 4)
            return base_domain+"image_bed%d.jpg" % img_index

    def get_real_url(self, randombackground, randomanimals, state):
        return base_domain + str(randombackground) + "-" + str(randomanimals) + "-" + str(state) + ".jpg"

    def get_random_place(self):
        all_imgs = PicDetail.objects.all()
        random_pics = []
        for img in all_imgs:
            if img.pic_name.startswith('1-'):
                continue
            if '-' not in img.pic_name:
                continue
            random_pics.append((img.pic_url, img.pic_description))
        pic_url, pic_description = random.choice(random_pics)
        return pic_url, pic_description

    def get_monkey_status(self, address):
        monkey_obj = MonkeyRecord.objects.filter(address=address).first()
        if not monkey_obj:
            return {"status": -1, "msg": "cannot find %s this user" % address}
        if int(time.time()) >= int(monkey_obj.go_home_time):
            # 当前时间超过了 该回家了
            monkey_obj.is_home = 1
            monkey_obj.save()
            return {"status": 2,
                    "msg": monkey_obj.description,
                    "pic_url": self.get_real_url(monkey_obj.randombackground,
                                                 monkey_obj.randomanimals,
                                                 monkey_obj.state)}
        pic_url, pic_description = self.get_random_place()
        return {"status": 1, "msg": pic_description, "pic_url": pic_url}

    def story_happen(self, **data):
        address = data.get("address")
        randombackground = data.get("randombackground")
        randomanimals = data.get("randomanimals")
        try:
            randomanimals = int(randomanimals)
        except Exception as e:
            randomanimals = 1
        state = data.get("state")
        # 该场景结束的时间，也就是发送照片的时间
        timestamp = data.get("timestamp")
        pic_url, pic_description = self.get_random_place()
        MonkeyRecord.objects.update_or_create(address=address, defaults=dict(randombackground=randombackground,
                                                                             randomanimals=randomanimals,
                                                                             state=state,
                                                                             go_home_time=int(timestamp),
                                                                             description=pic_description,
                                                                             is_home=0))
        query_result = self.get_monkey_status(address)
        if query_result.get("status") == 2:
            return query_result
        return {"status": 1, "msg": pic_description, "pic_url": pic_url}

    def playing(self):
        while True:
            all_out_monkeys = MonkeyRecord.objects.filter(is_home=0)
            for monkey in all_out_monkeys:
                if int(time.time()) >= monkey.go_home_time:
                    monkey.description = u"在家了"
                    monkey.is_home = 1
                    monkey.save()
                    continue
                pic_url, pic_description = self.get_random_place()
                monkey.description = pic_description
                monkey.save()
            time.sleep(5)

    def go_home(self, address):
        try:
            MonkeyRecord.objects.update_or_create(address=address, defaults=dict(is_home=1))
        except Exception as e:
            return {"status": -1, "msg": "go home failed, reason: %s" % str(e)}
        return {"status": 1, "msg": "success"}

api_process = ApiProcess()

if __name__ == "__main__":
    api = ApiProcess()
    test_data = {"address": "123", "randombackground":2, "randomanimals": 1, "state": 1, "timestamp": "1535824300"}
    print api.story_happen(**test_data)
    while True:
        print int(time.time())
        print api.get_monkey_status("123")
        time.sleep(3)
