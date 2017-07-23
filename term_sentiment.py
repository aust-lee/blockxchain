import sys
import json
import string



def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

#sent_file = open('AFINN-111.txt', 'r')
#tweet_file = open('data\stream_trump.json', 'r')
    scores = {}
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    not_in = {}

    for line in tweet_file:
        tweet = json.loads(line)
        tweet_mood = 0
        not_in_list = []
        try:
            for word in json.dumps(tweet["text"]).split():
                t_word = word.translate(None, string.punctuation).lower()
                if t_word in scores:
                    tweet_mood = scores[t_word] + tweet_mood
                else:
                    if t_word not in not_in:
                        not_in_list.append(t_word)
                        tweet_mood = tweet_mood + 0
            for word in not_in_list:
                if word in not_in:
                    not_in[word] = tweet_mood + not_in[word]
                else:
                    not_in[word] = tweet_mood
              

        except: 
          tweet_mood = 0

    for word in not_in:
        print "{} {}".format(word, not_in[word])


if __name__ == '__main__':
    main()
