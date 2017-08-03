# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pymongo import MongoClient
from bson import ObjectId
import csv


shop_set = set()
client = MongoClient('mongodb://localhost:27017/')

order_collection = client['aoao_test']['biz_order']
one_list = order_collection.find({"org_id": ObjectId("58afcf3b9982695c5aa5e18c")})
for one in one_list:
    shop_set.add(one['consignor']['name'])
shop_list = list(shop_set)

if __name__ == '__main__':
    listFile = open('listFile.csv', 'w')
    writer_ex = csv.writer(listFile)
    for shop in shop_list:
        writer_ex.writerow([shop])
    listFile.close()

