import requests
import tweepy
import fetchRedditImages
import os
import pickle
def authenticate():
    API_KEY = "api key"
    API_SECRET = "api secret"

    ACCESS_TOK = "access token"
    ACCESS_SECRET = "access secret"

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOK, ACCESS_SECRET)
    api = tweepy.API(auth)

    # api.update_status("This song is da bomb!!! tweeting from python again :))) https://www.youtube.com/watch?v=6Cy07t8jmA8")
    return api

def tweet_image(url, message):
    api = authenticate()
    #Saves file temporarily
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")


def tweet():
    submission = fetchRedditImages.fetchSubmission()


     #'Cleans' urls from invisible text
    post_urls = []
    try:
        post_file = open(r"previousPost.txt", "rb")
        post_urls = pickle.load(post_file)
    except:
        print("is empty")


        # print("URL: " + post_urls[len(post_urls) - 1])
        #Tweets the last url added to the file
    if len(post_urls) > 1:
        tweet_image(post_urls[len(post_urls) - 1], submission.title + " by: u/" + str(submission.author.name))
    else:
        tweet_image(post_urls[0], submission.title + " by: u/" + str(submission.author.name))

tweet()