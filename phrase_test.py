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
    print(phrase)
    while("[" in phrase):
        term = (phrase.split('['))[1].split(']')[0]
        phrase = phrase.replace('[' + term + ']', constant_dic[term][random.randrange(len(constant_dic[term]))], 1)
    return phrase
    
res = generate_phrase();
print(res)
if(len(res)>140):
    print('error')
