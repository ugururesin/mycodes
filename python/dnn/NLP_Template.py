### NLP TEMPLATE

## CURATE A DATASET
# Developing a Predictive Theory
# Transforming Text to Numbers
# Putting it all together in a Neural Network
# Understanding Neural Noise
# Analyzing Inefficiencies in the Network
# Reducing Noise by Reducing the Vocabulary

#Define a function that prints the review and it's label nicely
def pretty_print_review_and_label(i):
	print(labels[i] + "\t:\t" + reviews[i][:80] + "...")
 
g = open('reviews.txt', 'r')		#what we know!
reviews = list(map(lambda x:x[:-1],g.readlines()))
g.close()
 
g = open('labels.txt','r') 	#what we want to know!
labels = list(map(lambda x:x[:-1].upper(),g.readlines()))
g.close()

from collections import Counter		#for word count
import numpy as np

print("labels.txt \t : \t revies.txt\n")
pretty_print_review_and_label(2137)
pretty_print_review_and_label(12816)
pretty_print_review_and_label(6267)
pretty_print_review_and_label(21934)
pretty_print_review_and_label(4998)


## STEP1: Quick Theory Validation
from collections import Counter
import numpy as np

positive_counts = Counter()		#empty counter
negative_counts = Counter() 		#empty counter
total_counts = Counter()				#empty counter

for i in range(len(reviews)):
	if(labels[i] == 'POSITIVE'):
		for word in reviews[i].split(" "):
			positive_counts[word] +=1
			total_counts[word] +=1
	else:
			for word in reviews[i].split(" "):
			negative_counts[word] +=1
			total_counts[word] +=1
			
positive_counts.most_common()
negative_counts.most_common()

#Normalization
pos_neg_ratios = Counter()

for term,cnt in list(total_counts.most_common() ):
	if(cnt > 10):
		pos_neg_ratio = positive_counts[term] / float(negative_counts[term] +1)
		pos_neg_ratios[term] = pos_neg_ratio
		
for word,ratio in pos_neg_ratios.most_common()		
	if(ratio > 1):
		pos_neg_ratios[word] = np.log(ratio)
	else:
		pos_neg_ratios[word] = -np.log((1/(ratio+0.01)))
		
list(reversed(pos_neg_ratios.most_common() ))[0:30]

 
 ## STEP2: Creating the Input/Output Data
 
 vocab = set(total_counts.keys())
 vocab_size = len(vocab)
 print(vocab_size)
 
 import numpy as np
 
 layer_0 = np.zeros((1,vocab_size))	#create an empty vector
 layer_0
 
 word2index = {}
 
 for i,word in enumerate(vocab):
	word2index[word] = i
word2index

def update_input_layer(review):

	global layer_0
	
	#clear out previous state, reset the layer to be all 0s
	layer_0 *= 0
	for word in review.split(" "):
		layer_0[0][word2index[word] ] += 1

update_input_layer(reviews[0])


def get_target_for_label(label):
	if(label == 'POSITIVE'):
		return 1
	else:
		return 0
		
get_target_for_label(labels[0])


## STEP3: BUILDING A NN
import time
import sys
import numpy as np

#Let's tweak the network before to model these phenomena
class SentimentNetwork:
	def __init__(self, reviews, labels, hidden_nodes = 10, learning rate = 0.1):
	
		#set our random number generator
		np.random.seed(1)
		
		self.pre_process_data(reviews, labels)
		
		self.init_network(len(self.review_vocab), hidden_nodes, 1, learning_rate)
		
		
	def pre_process_data(self, reviews, labels):
		
		review_vocab = set()
		for review in reviews:
			for word in review.split(" "):
				review_vocab.add(word)
		self.review_vocab = list(review_vocab)
			
		label_vocab = set()
		for label in labels:
			label_vocab.add(label)
			
		self.label_vocab = list(label_vocab)
			
		self.review_vocab_size = len(self.review_vocab)
		self.label_vocab_size = len(self.label_vocab)
			
			self.word2index = {}
			for i, word in enumerate(self.review_vocab):
				self.word2index[word] = i
				
			self.label2index = {}
			for i, label in enumerate(self.label_vocab):
				self.label2index[label] = i
 
 
		
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 