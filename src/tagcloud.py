"""
    Project Name:   Twitter Tagcloud
    Author:         Alexandru Buliga
    Email:          bugaaa92@gmail.com
"""


import sys
import re
import logging
import json
from threading import currentThread, enumerate, Lock, Thread
from collections import Counter, OrderedDict
from datetime import datetime
import tweepy
import resource


class TweetRetriever:
    """
        Retrieves tweets using the Tweeter API provided by tweepy
        Performs authentication with OAuth protocol
    """


    def __init__(self, creds, stopwords):
        """
            Constructor method
            @param creds: dictionary containins authentication tokens
            @param stopwords: set of words that are not taken into account
        """

        self.stopwords = stopwords
        self.creds = creds

        # Result per page constant defined here
        self.RESULTS_PER_PAGE = 100

        # OAuth Authentication
        self.auth = tweepy.OAuthHandler(
            creds['consumer_key'], creds['consumer_secret'])
        self.auth.secure = True
        self.auth.set_access_token(
            creds['access_token'], creds['access_token_secret'])

        # Setting the Teepy API
        self.api = tweepy.API(self.auth)

        # Used to guarantee atomic access to the global counter
        self.lock = Lock()

        # Setting global word counter
        self.globalWordCounter = Counter()


    def doWork(self, tweetList):
        """
            Function associated with worker thread; gets all the words and its
            occurances in the tweetList and updated the global counter
            @param tweetList: a list of tweets for the worker thread
        """

        # Get the list of words
        wordList = []
        cleanWordList = []
        for tweetText in tweetList:
            wordList.extend(re.findall(r"[\w']+", tweetText.lower()))

        # Convert the strings to ascii by uncommenting the line after next
        for word in wordList:
            # word = word.encode('ascii', 'ignore')
            if word not in self.stopwords:
                cleanWordList.append(word)

        # Update the global counter with the local one
        with self.lock:
            self.globalWordCounter.update(Counter(cleanWordList))


    def run(self, durationInterval, wordCount):
        """
            Tweets retrieval method
            @param durationInterval: the duration of the data fetch process
            @param wordCount [optional]: how many results to show
        """

        counter = 0
        startTime = None
        tweetList = []

        if durationInterval <= 0:
            return

        # Get tweepy cursor
        cursor = tweepy.Cursor(self.api.search,
            q           = "a",
            count       = self.RESULTS_PER_PAGE,
            result_type = "recent",
            lang        = "en").items()

        # Iterate all tweets in the past durationInterval seconds using Cursor
        while True:
            try:
                tweet = cursor.next()
            except tweepy.TweepError:
                print "Error. Exceeded Twitter request limit.", \
                        "Try again in 15 minutes."
                break

            # Store info about the tweet
            postTime = tweet.created_at
            tweetList.append(tweet.text)
            
            if startTime:
                # Check if durationInterval has passed and we have to stop
                if abs((postTime - startTime).total_seconds()) > durationInterval:
                    # Start last worker thread
                    Thread(target = TweetRetriever.doWork,
                        args = (self, tweetList)).start()
                    break
            else:
                # Mark the current time of the first retrieved tweet and count
                # durationInterval seconds starting from here
                startTime = postTime

            counter += 1
            if counter == self.RESULTS_PER_PAGE:
                # Start worker thread
                Thread(target = TweetRetriever.doWork,
                    args = (self, tweetList)).start()
                counter = 0
                tweetList = []

        # Wait threads to finish their work
        main_thread = currentThread()
        for thread in enumerate():
            if thread is main_thread:
                continue
            thread.join()

        if (wordCount >= 0):
            # Count how many other words there are
            otherWordCounter = self.globalWordCounter.most_common()[wordCount::]
            otherCount = sum(count for _, count in otherWordCounter)

            # Update the global counter with the special word, other
            self.globalWordCounter = self.globalWordCounter.most_common(wordCount)
            self.globalWordCounter.append(('other', otherCount))
        else:
            self.globalWordCounter = self.globalWordCounter.most_common()
        
        # Write results to a local JSON file
        self.writeResult()
        

    def writeResult(self):
        """
            Write results to a local JSON file
        """

        wcList = []

        # Convert list elements to dictionary for pretty printing
        for elem in self.globalWordCounter:
            wcList.append(OrderedDict([('word', elem[0]), ('count', elem[1])]))

        with open('results.json', 'w') as out_file:
            json.dump(wcList, out_file, indent = 4, separators = (',', ': '))


def main():
    """
        Main function definition
    """

    # Disabling some ugly warnings
    logging.captureWarnings(True)

    # Verifying if the command-line arguments are passed
    if len(sys.argv) < 2:
        print "Error. Run: python tagcloud.py <duration> [<wordCount>]"
        sys.exit()

    # Getting the duration of the data fetch process
    durationInterval = sys.argv[1]
    wordCount = -1

    try:
        durationInterval = int(durationInterval)
    except ValueError:
        print "Error. Arguments must be numbers!"
        sys.exit()

    # If the word count argument is passed, get it
    if len(sys.argv) == 3:
        try:
            wordCount = int(sys.argv[2])
        except ValueError:
            print "Error. Arguments must be numbers!"
            sys.exit()

    # Start retrieving tweets
    tweetRetriever = TweetRetriever(resource.creds, resource.stopwords)
    tweetRetriever.run(durationInterval, wordCount)


"""
    Start main
"""
if __name__ == '__main__':
    main()
