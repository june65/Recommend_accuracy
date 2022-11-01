#api call
import requests

response = requests.get("https://api.doggly.co.kr/v1/public/product?limit=10000")

import json

datas = json.loads(response.text)

from recommend import *

# file_read  
def file_read(file):
    print("start file_read")

    dog_info_list=[]
    line = file.read().split('\n')
    for i in range(0, len(line) - 1):

        #dog_info = [product_name, dog_name, dog_weight, dog_breed, dog_age, dog_chest, dog_neck, dog_back, dog_leg, dog_size, brand]
        dog_info = line[i].split(',')
        dog_info.insert(0, i)
        dog_info_list.append(dog_info)

    print("successfully file_read")

    return dog_info_list  

data_file = open('./model.csv', 'r')
dog_data = file_read(data_file)

for j in range(1,len(dog_data)):

    for i in range(len(datas)):
        
        if dog_data[j][1] == datas[i].get("product_name"):

            product_uuid = datas[i].get("product_uuid")

            response_detail = requests.get("https://api.doggly.co.kr/v1/public/product/detail/" + product_uuid + "?limit=10000")
            
            datas_detail = json.loads(response_detail.text)

            response_product = requests.get("https://api.doggly.co.kr/v1/public/product/" + product_uuid )
            
            datas_product = json.loads(response_product.text)

    response_category = requests.get("https://api.doggly.co.kr/v1/public/category/product/" + product_uuid)

    datas_category = json.loads(response_category.text)

    important_size = ""
    important_category_name = ""

    for i in range(len(datas_category)):

        main_category = requests.get("https://api.doggly.co.kr/v1/public/category/find/" + datas_category[i].get("category_uuid"))

        main_important_size = json.loads(main_category.text)

        if main_important_size.get("important_size") != None:
            important_size = main_important_size.get("important_size")
            important_category_name = main_important_size.get("category_name")

    recommend(response_product.text,response_detail.text,important_size,important_category_name,dog_data[j])