import sys
import json
import string
import operator


def main():
    tweet_file = open(sys.argv[1])

#tweet_file = open('data\stream_trump.json', 'r')

    counting = {}
    total = 0
    for line in tweet_file:
        tweet = json.loads(line)
        total_words = 0
        count = 0
        try:
            t_word = json.dumps(tweet["entities"]["hashtags"][1]["text"]).lower()
            if t_word in counting:
                counting[t_word] = counting[t_word] + 1
            else:
                counting[t_word] = 1      
                
            
        except:
            hashtag = 0
    sorted_x = sorted(counting.items(), key=operator.itemgetter(1), reverse= True)

    top_ten = sorted_x[:10]

    for each in top_ten:
        print "{} {}".format(each[0], float(each[1]))

if __name__ == '__main__':
    main()




