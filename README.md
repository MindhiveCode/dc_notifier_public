# Nexus Slack Integration
Sends messages to a Slack Webhook when proposal vote count has changed by given amount.

## Installation
We use JSON for temporary storage so you'll want to set this up on a machine with non-ephemeral storage (aka not Heroku)

### Slack Application
You'll need to create a Slack application and then get a Webhook URL that you can post things to, you'll then use that in the next step.

### Server-Side Setup

In order for this to work properly, you need to setup the following environment variables. For graphing to work correctly, you'll need an AWS Bucket and corresponding API Keys with access to that Bucket.

    WEBHOOK_URL
    AWS_ACCESS_KEY_ID
    AWS_SECRET_KEY
    PROPOSAL_HASH
    AWS_BUCKET
    DELTA_SETTING

Crontab settings - modify the directories in brackets to correspond with your setup

    */15 * * * * cd /home/[git repo directory] && /usr/bin/python3 /home/[git repo directory]/vote_watcher.py >> /home/[logging directory]/vote_check.log 2>&1

