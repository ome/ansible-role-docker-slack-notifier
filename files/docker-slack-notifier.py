#!/usr/bin/env python
# Listen to Docker container events and send a slack notification

import docker
import json
import re
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
SLACK_WEBHOOK = "https://hooks.slack.com/services/%s" % cfg['slack_token']
client = docker.DockerClient(version='auto')

for event in client.events():
    e = json.loads(event)
    action = e['Action']
    typ = e['Type']
    if typ == 'container' and re.match(cfg['eventmatch']['action'], action):
        name = e['Actor']['Attributes']['name']
        image = e['Actor']['Attributes']['image']
        if (re.match(cfg['eventmatch']['image'], image) and
                re.match(cfg['eventmatch']['container'], name)):
            msg = "%s %s: %s" % (image, action, name)
            print(msg)
            send_notification(msg)
