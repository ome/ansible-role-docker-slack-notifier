Docker Slack Notifier
=====================

Sends notifications to Slack when a Docker container is created, started, stopped or destroyed.


Dependencies
------------

Docker must be running (not handled by this role).


Role Variables
--------------

Required variables:
- `docker_slack_notifier_token`: Slack web-hook token.

Optional variables:
- `docker_slack_notifier_basedir`: Installation directory
- `docker_slack_notifier_channel`: Slack #channel
- `docker_slack_notifier_username`: Slack username
- `docker_slack_notifier_icon`: Slack :emoji:


Example Playbook
----------------

    - hosts: all
      roles:
        - role: openmicroscopy.docker
        - role: openmicroscopy.docker-slack-notifier
          docker_slack_notifier_channel: "#notifications"
          docker_slack_notifier_username: "Docker {{ ansible_hostname }}"
          docker_slack_notifier_token: XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXX          


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
