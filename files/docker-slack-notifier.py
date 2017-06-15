#!/usr/bin/env python
# Listen to Docker container events and send a slack notification

import docker
import json
import requests
import sys
import yaml


def send_notification(msg):
    message = {
        "channel": cfg['channel'],
        "username": cfg['username'],
        "text": str(msg),
        "icon_emoji": cfg['icon'],
    }
    requests.post(SLACK_WEBHOOK, data=json.dumps(message),
                  headers={"Content-Type": "application/json"})


with open(sys.argv[1]) as fh:
    cfg = yaml.load(fh)
print cfg
SLACK_WEBHOOK = "https://hooks.slack.com/services/%s" % cfg['slack_token']
client = docker.DockerClient()

for event in client.events():
    e = json.loads(event)
    action = e['Action']
    typ = e['Type']
    name = e['Actor']['Attributes']['name']
    if typ == 'container' and action in ('create', 'start', 'stop', 'destroy'):
        image = e['Actor']['Attributes']['image']
        msg = "%s %s: %s" % (image, action, name)
        print(msg)
        send_notification(msg)
