#!/usr/bin/python
# -*- coding: utf8 -*-

#Author Παναγιώτης Πράττης/Panagiotis Prattis

'''
Program which shows client's Twitter friends and then checks if two of them 
selected by the user have any common friends and prints them.
'''
import time
import tweepy

auth = tweepy.OAuthHandler("key", "key") #(key, secret)
auth.set_access_token("token", "token") #(token, secret token)


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

client = tweepy.API(auth)

friends = client.friends()

for friend in tweepy.Cursor(client.friends).items(200): #show max 200 friends
    print (friend.name)

user1 = raw_input("Please enter 1st twitter user");
user2 = raw_input("Please enter 2nd twitter user");
ids1 = []
for page in tweepy.Cursor(api.followers_ids, screen_name=user1).pages(5):
    ids1.extend(page)
    time.sleep(10)
    
ids2 = []
for page in tweepy.Cursor(api.followers_ids, screen_name=user2).pages(5):
    ids2.extend(page)
    time.sleep(10)
    
#print len(ids)
'''
for x in range(0,len(ids1)):
    print ids1[x];
for x in range(0,len(ids2)):
    print ids2[x];
'''

n = 0;
for x in range(0,len(ids1)):
    #print "I came here1";
    for y in range(0,len(ids2)):
        #print "I came here2";
        if(ids1[x] == ids2[y]):
            print "This is a common friend: " + ids1[x] + "\n";
            n =1;
            break;

if(n==0):
    print "No common friends";
