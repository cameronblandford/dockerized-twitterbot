# Dockerized Twitter Bot

This twitter bot uses [Alpine](https://alpinelinux.org/) Linux with a [BusyBox](https://busybox.net/about.html) crond job scheduler to provide a low-footprint and easy to use twitter bot. The cronjob setup is based off of [Andy's](https://github.com/andyshinn) [gist](https://gist.github.com/andyshinn/3ae01fa13cb64c9d36e7).

## Prerequisites
* You must either have a `secrets.py` file containing your Twitter app and token keys and secrets, or simply replace those variables with the respective strings. Visit [https://apps.twitter.com/](https://apps.twitter.com/) to get yourself the required credentials!

## To change what the bot does:
* All you have to do is edit the internals of `tweet.py`! The main method is called every hour by default. This can be edited in the jobs.txt file, using [standard cronjob syntax](https://crontab.guru).

## Quickstart

### Run locally
* `$ git clone <this repo>`
* `$ cd dockerized-twitterbot`
* `$ docker-compose up -d`

### Run on a dedicated server:
* [Set up a digitalocean docker server](https://www.digitalocean.com/community/tutorials/how-to-use-the-digitalocean-docker-application), or any other server that works to your liking ([hyper.sh](https://hyper.sh/) is cheaper ($1 as opposed to $5 per month) but not pre-configured).
* SSH into your server.
* Install docker and docker-compose if needed.
* `$ git clone <this repo>`
* `$ cd dockerized-twitterbot`
* `$ docker-compose up -d`

### Debugging
* all stdout from tweet.py is dumped into /log.txt
* `$ docker exec -ti <your container name> /bin/ash` (`ash`, not `bash`) will open up the container's terminal
* `$ tail -f log.txt` will let you livestream any updates to the logs.
