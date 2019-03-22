'''
Create a slack API token for the codingnomads workspace.

Using the slackclient package, fetch all comments that include links
from the python-resources channel.

Store the links in a JSON file that has the following form:
[
    {
        "link": "the fetched URL",
        "description": "short blurb describing the resource (if available)",
        "date_added": "when was it posted?",
        "read": False  # defaults to False, change to True if you read it
        "rating": 0  # on a scale from 1-10, initially 0
        "comments": [
            "a list of strings",
            "with comments on the resource",
        ]
        "starred": False,  # defaults to False, change to True if you think it's great
    },
    # next link item
]

We will continue to work with this data throughout the week, so make sure to complete it!

'''

from slackclient import SlackClient
from pprint import pprint
import json
from datetime import datetime

token = "xoxp-561901429298-574804874820-582472767798-199636c2c6e4d0bfca791e6f27b876f7"      # found at https://api.slack.com/web#authentication

sc = SlackClient(token)

slack_args = {'python_resources': 'CGUDWETHR'}

hist = sc.api_call('channels.history', channel=slack_args['python_resources'])

# pprint(hist)
# print(len(hist))
#
# for i in hist:
#     print(i)

slack_messages = hist['messages']


database_list = []
database_dict = {}

# [4:9]

for i in slack_messages:
   # pprint(i)
   if 'http' in i['text']: # this text is a listed dictionary
       pprint(i)
       link = i['text'].strip('<>')
       try:
           star = i['is_starred']
       except:
           pass
       read = False
       time = float(i['ts'])
       time = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
       description1 = i['attachments'][0]
       description = description1['text']
       database_list.append([{'link': link,
                              'description': description,
                              'date_added': time,
                              'read': False,
                              'rating': 0,
                              }])
       # date_added = datetime.utcfromtimestamp()
       # print(date_added)


pprint(database_list)

with open('slack_jason_dump.txt', 'w') as f:
   json.dump(database_list, f)