import snscrape.modules.twitter as sntwitter
import pandas as pd
from flask import Blueprint, request
from flask import jsonify
# import instaloader
from datetime import datetime
from itertools import dropwhile, takewhile
import requests
from bs4 import BeautifulSoup
import selenium

from selenium import webdriver
import urllib.request

import json
from main import predict



api = Blueprint('api', __name__)

@api.route('/twitter', methods=['POST'])
def twitter():
    param = request.get_json()
    if param['exclude']:
        param['exclude'] = param['exclude'].split(',')

    # return param['exclude']
    # Creating list to append tweet data to
    tweets_list2 = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    # for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pisang goreng since:2022-12-01 until:2022-12-31').get_items()):
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('{} since:{} until:{}'.format(param['query'],param['start'],param['end']), None, True).get_items()):
        if i>param['limit']:
            break
        if any(twt in tweet.content.lower() for twt in param['exclude']):
            print("exclude")
        else:
            tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
        
    # Creating a dataframe from the tweets list above
    # tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
    return jsonify(tweets_list2)

@api.route('/predict', methods=['POST'])
def main():
    # load json data
    data = json.loads(request.data)

    # get data
    question = data['text']

    # predict
    label, score = predict.main(question)
    result = {
        'label': label,
        'score': score
    }
    
    return result
