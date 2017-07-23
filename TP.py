"""afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.



  def lines(fp):
    print str(len(fp.readlines()))
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()



    
def lines(fp):
    print str(len(fp.readlines()))"""
""""

import string
words = "hello world it is me, austin."

word = words.split()

for t_word in word:
    print t_word.translate(None, string.punctuation)

sent_file = open("AFINN-111.txt", "r")
print sent_file
"""

words = "hello how are world you bad word"
not_in = {}
tweet_mood = 0
word_dict = {"hello": 2, "world": 4}


for word in words.split():
    if word in word_dict:
        tweet_mood = word_dict[word] + tweet_mood
    else:
        not_in[word] = 0

for word in not_in:
    not_in[word] = not_in[word] + tweet_mood

for word in not_in:
    print "{} {}".format(word, not_in[word])


