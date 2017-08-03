# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pymongo import MongoClient
from bson import ObjectId
import math
from datetime import datetime, timedelta
import csv

# 地球半径
EARTH_RADIUS = 6372000
# 2017-02-24T10:27:25.372Z


item_num = {
    '0': "10:30-10:45", '1': "10:46-11:00", '2': "11:01-11:15", '3': "11:16-11:30",
    '4': "11:31-11:45", '5': "11:46-12:00", '6': "12:01-12:15", '7': "12:16-12:30",
    '8': "12:31-12:45", '9': "12:46-13:00", '10': "13:01-13:15", '11': "13:16-13:30",
    '12': "13:31-13:45", '13': "13:46-14:00", '14': "14:01-14:15", '15': "14:16-14:30",
    '16': "14:31-14:45", '17': "14:46-15:00", '18': "15:01-15:15", '19': "15:16-15:30",
    '20': "15:31-15:45", '21': "15:46-16:00", '22': "16:01-16:15", '23': "16:16-16:30",
    '24': "16:31-16:45", '25': "16:46-17:00", '26': "17:01-17:15", '27': "17:16-17:30",
    '28': "17:31-17:45", '29': "17:46-18:00", '30': "18:01-18:15", '31': "18:16-18:30",
    '32': "18:31-18:45", '33': "18:46-19:00", '34': "19:01-19:15", '35': "19:16-19:30",
    '36': "19:31-19:45", '37': "19:46-20:00", '38': "20:01-20:15", '39': "20:16-20:30",
    '40': "20:31-20:45", '41': "20:46-21:00", '42': "21:01-21:15", '43': "21:16-21:30",
    '44': "21:31-21:45", '45': "21:46-22:00", '46': "22:01-22:15", '47': "22:16-22:30",
}


def get_beeline_distance(src_lng, src_lat, dst_lng, dst_lat):
    dx = src_lng - dst_lng  # 经度差值
    dy = src_lat - dst_lat  # 差值纬度
    b = (src_lat + dst_lat) / 2.0  # 平均纬度
    Lx = math.radians(dx) * EARTH_RADIUS * math.cos(math.radians(b))  # 东西距离
    Ly = EARTH_RADIUS * math.radians(dy)  # 南北距离
    distance = math.sqrt(Lx * Lx + Ly * Ly)  # 用平面的矩形对角距离公式计算总距离
    return int(round(distance))


shop_set = set()
client = MongoClient('mongodb://localhost:27017/')

order_collection = client['aoao_test']['biz_order']
one_list = order_collection.find({"org_id": ObjectId("58afcf3b9982695c5aa5e18c")})
for one in one_list:
    shop_set.add(one['consignor']['name'])
print(len(shop_set))

# start_time = datetime(2017, 2, 26, 10, 30)
# end_time = start_time + timedelta(hours=12)

start_list = [
    # datetime(2017, 7, 1, 10, 30),
    # datetime(2017, 7, 2, 10, 30),
    # datetime(2017, 7, 3, 10, 30),
    # datetime(2017, 7, 4, 10, 30),
    # datetime(2017, 7, 5, 10, 30),
    # datetime(2017, 7, 6, 10, 30),
    datetime(2017, 7, 7, 10, 30),
    datetime(2017, 7, 8, 10, 30),
    datetime(2017, 7, 9, 10, 30),
    datetime(2017, 7, 10, 10, 30),
    datetime(2017, 7, 11, 10, 30),
    datetime(2017, 7, 12, 10, 30),
    datetime(2017, 7, 13, 10, 30),
]


def day_func(start_time, writer):
    end_time = start_time + timedelta(hours=12)
    for shop in shop_set:
        # shop_item = dict()
        # 生成店铺集合
        num_distance = {
            "shop": shop,
            "date": start_time,
            u"a圈": {
                "10:30-10:45": 0, "10:46-11:00": 0, "11:01-11:15": 0, "11:16-11:30": 0,
                "11:31-11:45": 0, "11:46-12:00": 0, "12:01-12:15": 0, "12:16-12:30": 0,
                "12:31-12:45": 0, "12:46-13:00": 0, "13:01-13:15": 0, "13:16-13:30": 0,
                "13:31-13:45": 0, "13:46-14:00": 0, "14:01-14:15": 0, "14:16-14:30": 0,
                "14:31-14:45": 0, "14:46-15:00": 0, "15:01-15:15": 0, "15:16-15:30": 0,
                "15:31-15:45": 0, "15:46-16:00": 0, "16:01-16:15": 0, "16:16-16:30": 0,
                "16:31-16:45": 0, "16:46-17:00": 0, "17:01-17:15": 0, "17:16-17:30": 0,
                "17:31-17:45": 0, "17:46-18:00": 0, "18:01-18:15": 0, "18:16-18:30": 0,
                "18:31-18:45": 0, "18:46-19:00": 0, "19:01-19:15": 0, "19:16-19:30": 0,
                "19:31-19:45": 0, "19:46-20:00": 0, "20:01-20:15": 0, "20:16-20:30": 0,
                "20:31-20:45": 0, "20:46-21:00": 0, "21:01-21:15": 0, "21:16-21:30": 0,
                "21:31-21:45": 0, "21:46-22:00": 0, "22:01-22:15": 0, "22:16-22:30": 0,
            },
            u"b圈": {
                "10:30-10:45": 0, "10:46-11:00": 0, "11:01-11:15": 0, "11:16-11:30": 0,
                "11:31-11:45": 0, "11:46-12:00": 0, "12:01-12:15": 0, "12:16-12:30": 0,
                "12:31-12:45": 0, "12:46-13:00": 0, "13:01-13:15": 0, "13:16-13:30": 0,
                "13:31-13:45": 0, "13:46-14:00": 0, "14:01-14:15": 0, "14:16-14:30": 0,
                "14:31-14:45": 0, "14:46-15:00": 0, "15:01-15:15": 0, "15:16-15:30": 0,
                "15:31-15:45": 0, "15:46-16:00": 0, "16:01-16:15": 0, "16:16-16:30": 0,
                "16:31-16:45": 0, "16:46-17:00": 0, "17:01-17:15": 0, "17:16-17:30": 0,
                "17:31-17:45": 0, "17:46-18:00": 0, "18:01-18:15": 0, "18:16-18:30": 0,
                "18:31-18:45": 0, "18:46-19:00": 0, "19:01-19:15": 0, "19:16-19:30": 0,
                "19:31-19:45": 0, "19:46-20:00": 0, "20:01-20:15": 0, "20:16-20:30": 0,
                "20:31-20:45": 0, "20:46-21:00": 0, "21:01-21:15": 0, "21:16-21:30": 0,
                "21:31-21:45": 0, "21:46-22:00": 0, "22:01-22:15": 0, "22:16-22:30": 0,
            },
            u"c圈": {
                "10:30-10:45": 0, "10:46-11:00": 0, "11:01-11:15": 0, "11:16-11:30": 0,
                "11:31-11:45": 0, "11:46-12:00": 0, "12:01-12:15": 0, "12:16-12:30": 0,
                "12:31-12:45": 0, "12:46-13:00": 0, "13:01-13:15": 0, "13:16-13:30": 0,
                "13:31-13:45": 0, "13:46-14:00": 0, "14:01-14:15": 0, "14:16-14:30": 0,
                "14:31-14:45": 0, "14:46-15:00": 0, "15:01-15:15": 0, "15:16-15:30": 0,
                "15:31-15:45": 0, "15:46-16:00": 0, "16:01-16:15": 0, "16:16-16:30": 0,
                "16:31-16:45": 0, "16:46-17:00": 0, "17:01-17:15": 0, "17:16-17:30": 0,
                "17:31-17:45": 0, "17:46-18:00": 0, "18:01-18:15": 0, "18:16-18:30": 0,
                "18:31-18:45": 0, "18:46-19:00": 0, "19:01-19:15": 0, "19:16-19:30": 0,
                "19:31-19:45": 0, "19:46-20:00": 0, "20:01-20:15": 0, "20:16-20:30": 0,
                "20:31-20:45": 0, "20:46-21:00": 0, "21:01-21:15": 0, "21:16-21:30": 0,
                "21:31-21:45": 0, "21:46-22:00": 0, "22:01-22:15": 0, "22:16-22:30": 0,
            }
        }

        list_order = order_collection.find({"org_id": ObjectId("58afcf3b9982695c5aa5e18c"), "consignor.name": shop,
                                            "created_at": {"$gt": start_time, "$lt": end_time}})
        for list_one in list_order:
            # print "=", list_one['created_at']
            consignor = list_one['consignor']['bd_poi']
            consignee = list_one['consignee']['bd_poi']
            ret = get_beeline_distance(consignor[0], consignor[1], consignee[0], consignee[1])
            if ret < 500:
                num_item = (list_one['created_at'] - start_time).seconds // 900
                num_distance[u"a圈"][str(item_num[str(num_item)])] += 1
            elif ret < 1500:
                num_item = (list_one['created_at'] - start_time).seconds // 900
                num_distance[u"b圈"][str(item_num[str(num_item)])] += 1
            else:
                num_item = (list_one['created_at'] - start_time).seconds // 900
                num_distance[u"c圈"][str(item_num[str(num_item)])] += 1
        print num_distance['shop']
        writer.writerow([str(start_time)])
        for key in num_distance:
            writer.writerow([key, num_distance[key]])

if __name__ == '__main__':
    csvFile = open('csvFile.csv', 'w')
    writer_ex = csv.writer(csvFile)
    for item_day in start_list:
        day_func(item_day, writer_ex)
    csvFile.close()

