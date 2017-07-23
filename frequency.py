import sys
import json
import string



def main():
      tweet_file = open(sys.argv[1])

#sent_file = open('AFINN-111.txt', 'r')
#tweet_file = open('data\stream_trump.json', 'r')

      counting = {}
      total = 0
      for line in tweet_file:
          tweet = json.loads(line)
          total_words = 0
          count = 0
          try:
              for word in json.dumps(tweet["text"]).split():
                  t_word = word.translate(None, string.punctuation).lower()
                  total = total + 1
                  if t_word in counting:
                        counting[t_word] = counting[t_word] + 1
                  else:
                        counting[t_word] = 1
                  
                  
                  
                  

          except:
                total = total


      totaling = {}
      for word in counting:
            totaling[word] = float(float(counting[word])/float(total))

      for word in totaling:
            print "{} {}".format(word, totaling[word])


if __name__ == '__main__':
      main()
