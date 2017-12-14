# coding=utf-8

import os
import random
import tweepy
from keys import *
from constants import *
from time import *

file = open(os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), "phrases.txt"),'r')
phrases = list(file)
file.close()




def generate_phrase():
    phrase = phrases[random.randrange(len(phrases))]
    while("[" in phrase):
        term = (phrase.split('['))[1].split(']')[0]
        phrase = phrase.replace('[' + term + ']', constant_dic[term][random.randrange(len(constant_dic[term]))], 1)
    return phrase


def tweet(text):
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    try:
        api.update_status(text)
    except tweepy.error.TweepError as e:
        print(text)
        log(e.message)
    else:
        log("Tweeted: " + text)


def log(message):
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, "jddtvbot.log"), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + message)


if __name__ == "__main__":
    while(True):
        tweet_text = generate_phrase()
        while(len(tweet_text)>140):
            print(tweet_text)
            tweet_text = generate_phrase()
        tweet(tweet_text)
        sleep(900)