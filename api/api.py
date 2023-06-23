
from flask import Blueprint, request, jsonify
import json
# import psycopg2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
import time

from module.gpt.gpt import sentiment
# from module.twitter.main import twitter

headers = {
    'origin': 'https://www.tokopedia.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'application/json, text/plain, */*',
    'authority': 'www.tokopedia.com'
    }

api = Blueprint('api', __name__)

# @api.route('/twitter', methods=['POST'])
# def twitter():
#     return twitter()

@api.route('/')
def test():
    return "Sentimetric ready for analyzes"

@api.route('/predict', methods=['POST'])
def predicts():
    data = json.loads(request.data)
    result = []
    db = psycopg2.connect(database="marketear-dev",
                        host="localhost",
                        user="sail",
                        password="password",
                        port="5432")
    # except Error as e:
        # print(e)

    for x in data:
        # predict
        # label, score = predict.main(x["text"])
        sentiments, emotion = sentiment(data["text"])
        result.append({
            'label': sentiments,
            'score': emotion,
            'emotion': emotion
        })
        update = "update intents set sentiment = '{}' where id = {}".format(sentiments,x["id"])
        cursor = db.cursor()
        cursor.execute(update)
        db.commit()

    db.close()
    data = {
        "predicted" : len(result),
        "message" : "Success Predict Sentiment"
    }
    return jsonify(data)

@api.route('/test-predict', methods=['POST'])
def main():
    data = json.loads(request.data)
    # label, score = predict.main(data["text"])
    sentiments, emotion = sentiment(data["text"])
    # return sentiments
    data = {
        'label': sentiments,
        'emotion': emotion,
        'score': emotion
    }

    return jsonify(data)

@api.route('tokopedia')
def tokped_get():
    driver = webdriver.Chrome()
    res = driver.get("https://www.tokopedia.com/search?navsource=&page=1&q=pepsodent&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=product")
    counter_page = 0
    datas = []

    # while counter_page < 3:
    #   for _ in range(0, 6500, 500):
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 1000)")
    time.sleep(1)

    elements = driver.find_elements(by=By.CLASS_NAME, value='css-12sieg3')
    for element in elements:
        img = element.find_element(By.CLASS_NAME, 'css-1q90pod').get_attribute('src')
        name = element.find_element(By.CLASS_NAME, 'css-3um8ox').text
        price = element.find_element(by=By.CLASS_NAME, value='css-1ksb19c').text
        city = element.find_element(by=By.CLASS_NAME, value='css-1kdc32b').text
        shop = element.find_element(by=By.CLASS_NAME, value='prd_link-shop-name').text
        rating = element.find_element(by=By.CLASS_NAME, value='prd_rating-average-text').text
        sold = element.find_element(by=By.CLASS_NAME, value='prd_label-integrity').text
        
        datas.append({
            'img': img,
            'name': name,
            'price': price,
            'city': city,
            'shop': shop,
            'rating': rating,
            'sold': sold,
        })


        # counter_page += 1
        # next_page = driver.find_element(by=By.XPATH, value="//button[@class='css-16uzo3v-unf-pagination-item' and text()='" + str(counter_page + 1) + "']")
        # next_page.click()
    
    return datas
    # return jsonify(res)

@api.route('shopee')
def shopee_get():
    driver = webdriver.Chrome()
    res = driver.get("https://shopee.co.id/search?keyword=pepsodent")
    # counter_page = 0
    datas = []

    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 500)")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 1000)")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 1300)")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 1310)")
    time.sleep(2)

    elements = driver.find_elements(by=By.CLASS_NAME, value='shopee-search-item-result__item')
    for element in elements:
        img = element.find_element(By.CLASS_NAME, 'vc8g9F').get_attribute('src')
        name = element.find_element(By.CLASS_NAME, 'Cve6sh').text
        price = element.find_element(by=By.CLASS_NAME, value='ZEgDH9').text
        city = element.find_element(by=By.CLASS_NAME, value='zGGwiV').text
        # shop = element.find_element(by=By.CLASS_NAME, value='prd_link-shop-name').text
        # rating = element.find_element(by=By.CLASS_NAME, value='prd_rating-average-text').text
        sold = element.find_element(by=By.CLASS_NAME, value='r6HknA').text
        
        datas.append({
            'img': img,
            'name': name,
            'price': price,
            'city': city,
            # 'shop': shop,
            # 'rating': rating,
            'sold': sold,
        })

    return datas