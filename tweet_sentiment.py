import json
import sys
import string


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    for line in tweet_file:
        tweet = json.loads(line)
        tweet_mood = 0
        try:
            for word in json.dumps(tweet["text"]).split():
                t_word = word.translate(None, string.punctuation)
                if t_word in scores:
                    tweet_mood = scores[t_word] + tweet_mood
                else:
                    tweet_mood = tweet_mood + 0
            print tweet_mood

        except: 
            print tweet_mood


if __name__ == '__main__':
    main()




