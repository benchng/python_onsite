from slackclient import SlackClient

token = "xoxp-561901429298-574804874820-582472767798-199636c2c6e4d0bfca791e6f27b876f7"      # found at https://api.slack.com/web#authentication

#https://codingnomads2019.slack.com/messages/CGKALBXC6

sc = SlackClient(token)
print (sc.api_call("api.test"))
print (sc.api_call("channels.info", channel="CGKALBXC6"))
print (sc.api_call(
        "chat.postMessage", channel="#python", text="Hello from Python! :tada:",
        username='benbot', icon_emoji=':robot_face:'
))
