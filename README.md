# dockerized-twitterbot

This twitter bot uses [Alpine](https://alpinelinux.org/) Linux with a [BusyBox](https://busybox.net/about.html) crond job scheduler to provide a low-footprint and easy to use twitter bot.

## Prerequisites
* The current setup requires that you have a nouns.txt file, containing a list of nouns, and a bannedwords.txt file, containing a list of words that, if included in a tweet, will force the tweet to be thrown out.
* The current setup also requires that you have a secrets.txt file containing your Twitter app and token keys and secrets.

## To change what the bot does:
* All you have to do is edit the internals of tweet.py! The main method is called every minute by default. This can be edited in the jobs.txt file, using standard cronjob syntax.

## Quickstart

### Run locally
* Pull code
* `$ docker-compose up -d`

### Run on a dedicated server:
* Rent a digital ocean server pre-configured for docker, ssh into the server
* Install docker-compose if needed.
* Pull this git repo. 
* cd into the repo and '$ docker-compose up -d` to start the docker container.

### Debugging
* all stdout from tweet.py is dumped into /log.txt
* `$ docker exec -ti dockerizedtwitterbot_web_1 /bin/ash` (`ash`, not `bash`) will open up the container's terminal
* `$ tail -f log.txt` will let you stream any updates to the logs.
