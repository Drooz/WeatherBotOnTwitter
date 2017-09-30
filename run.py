
import schedule
import time

def job():
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
 
    import tweepy, time, sys, urllib, json
 
    # enter the corresponding information from your Twitter application/Forecast.io API KEY/lat and long:
    CONSUMER_KEY = '6JS1Xbvz3rIxnsssNBREo2mGJ'
    CONSUMER_SECRET = 'PzywGac8svUZhuR3iRWLqMk4Jl6fK101ADjnIHTSqLN8dbcRLJ'
    ACCESS_KEY = '913965204089851905-6JfjJcpjlMrFDeMx6L7M5oSeVqryo4R'
    ACCESS_SECRET = 'clm6hqpi0YeVtJhlECeOpKBrD4yq2oQTikt1gNDo0M1w8'
    FORECAST_IO_APIKEY ='21235c0f78d37a6e65f95070021a3f64'
    LATITUDE = '41.0082'
    LONGITUDE = '28.9784'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    url = "https://api.forecast.io/forecast/" + FORECAST_IO_APIKEY + "/" + LATITUDE + "," + LONGITUDE
    response = urllib.request.urlopen(url);
    s1 = response.read()
    data = json.loads(s1.decode())

    # print json.dumps(data, sort_keys=True, indent=4)
    
    temperature = str(int(round(data['currently']['temperature'])))
    degree_sign = u'\N{DEGREE SIGN}'
    summary = data['daily']['summary']
    today = data['hourly']['summary']
    # Conv to C
    tempf = str(int((int(temperature)-32)*5/9))
    #END Conv 

    tweet = "It's " + tempf + degree_sign + "C. " + today + " " + summary

    if len(tweet) > 140:
        tweet = "It's " + tempf + degree_sign + "C. " + today
    
    print (tweet)
    api.update_status(status=tweet)

schedule.every(1).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)