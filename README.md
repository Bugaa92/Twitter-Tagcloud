# Twitter-Tagcloud

1.Installation
------------

Install pip (python should already be installed):

    sudo apt-get install python-pip

Install tweepy:
    
    sudo pip install tweepy
    sudo easy_install -U pip # for special dependencies

Then install Redis:

    sudo pip install redis
    sudo apt-get install redis-server # install redis server

Download this repo:

    git clone https://github.com/Bugaa92/Twitter-Tagcloud.git
    cd Twitter-Tagcloud/src
Edit resource.py and add your personal tokens following the tips inside the comments. 


2.Running the version using Counter (Python collection)
------------
    # run from src/ folder
    python tagcloud.py <duration> [<wordCount>]


3.Running the version using Redis
------------
    # run from src/ folder
    redis-server # run local redis server
    python redis_tagcloud.py <duration> [<wordCount>]


4.Cleaning
------------
    rm results.json

Developed with: Python version 2.7.6


5.Documentation
-------------
  - [Python Documentation 2](https://docs.python.org/2/)
  - [Tweepy Documentation](http://tweepy.readthedocs.org/en/v3.2.0/)
  - [Redis-py Documentation](https://redis-py.readthedocs.org/)
  - [Twitter Developers](http://dev.twitter.com/)
