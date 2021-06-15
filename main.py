import nltk.data
nltk.download('punkt')

import joblib as jb
from  profanity_check  import  predict_prob

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("C:/Users/Dell Latitude/Desktop/1.txt")
data = fp.read()

print ('\n-----\n'.join(tokenizer.tokenize(data)))

sents = nltk.sent_tokenize(data)

 for sents in data :
      b=predict_prob(sents)
      print ("degree of sentence profanity =" b)


