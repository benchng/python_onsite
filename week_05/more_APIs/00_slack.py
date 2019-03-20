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

token = "xoxp-561901429298-574804874820-582472767798-199636c2c6e4d0bfca791e6f27b876f7"      # found at https://api.slack.com/web#authentication

#https://codingnomads2019.slack.com/messages/CGKALBXC6

sc = SlackClient(token)

slack_args = {'python_resources': 'CGUDWETHR'}

hist = sc.api_call('channels.history', channel=slack_args['python_resources'])

pprint(hist)
print(len(hist))

slack_messages = hist['message']

for i in slack_messages:
    print(i['title'])
    print(i['text'])
    print(i['ts'])