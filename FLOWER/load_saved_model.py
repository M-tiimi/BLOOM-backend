from string import punctuation
from os import listdir
from numpy import array
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from nltk.corpus import stopwords
import string
import numpy as np
import os
import h5py


def load_doc1(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

def clean_doc1(doc):
	# split into tokens by white space
	tokens = doc.split()
	# remove punctuation from each token
	table = str.maketrans('', '', string.punctuation)
	tokens = [w.translate(table) for w in tokens]
	# remove remaining tokens that are not alphabetic
	tokens = [word for word in tokens if word.isalpha()]
	# filter out stop words
	stop_words = set(stopwords.words('english'))
	tokens = [w for w in tokens if not w in stop_words]
	# filter out short tokens
	tokens = [word for word in tokens if len(word) > 1]
	return tokens

def handle_data(data):
	max_length = 422
	cleaned_data = [clean_doc1(data)]
	#encode data
	sequenced_data = encode_data(cleaned_data)
	#pad data
	handeled_data = pad_sequences(sequenced_data, maxlen=max_length, padding='post')
	
	return handeled_data

def encode_data(data):
	tokenizer = Tokenizer()
	
	tokenizer.fit_on_texts(data)
	
	encoded_data = tokenizer.texts_to_sequences(data)
	
	
	return encoded_data



def make_predictions(data):
	print('hi i try to predict')

	# load model
	model = load_model("FLOWER\latest_model.h5")
	model.summary()
	sequenced_data = handle_data(data)
	
	predictions = model.predict(sequenced_data, verbose = 0)
	if predictions > 0.5: 
		print(predictions, ' data is positive')
		return predictions.tolist(), ' data is positive'
	else:
		print(predictions,' data is negative')
		return predictions.tolist(), ' data is negative'


datapos= """ niagara niagara ( r ) bob gosse's niagara niagara follows a blueprint not unlike a lot of young-lovers-on-the-road movies . 
wild marcy ( robin tunney ) and calm seth ( henry thomas ) meet cute , literally running into each other while shoplifting at a local store . 
a mere couple of scenes later , the two embark on a journey to toronto from their small , unnamed american town in pursuit of a rare doll that marcy desperately wants . 
along the way , true love inevitably blossoms . 
what sets niagara niagara apart , though , is that marcy is afflicted with tourette's syndrome , a neurological disorder that causes sudden muscle and vocal tics . 
tunney , displaying an acting range not hinted at in the teenage witch thriller the craft , delivers an astonishing performance that won her the best actress prize at last year's venice film festival . 
to term her work a tour-de-force is not to imply that she attacks the scenery ; tunney's effectiveness lies in her modulation and vulnerability , which makes her depiction of marcy's illness--which often causes her to act violently--that much more convincing and tragic . 
she and the nicely subtle thomas develop a sweetly innocent and beguilingly off-kilter chemistry . 
their journey hits a few rough spots creatively along the way , mostly the fault of writer matthew weiss . 
a detour involving a kindly widower ( michael parks ) who takes the couple in brings the story to a screeching halt , and the key character of a trigger-happy pharmacist ( stephen lang ) is highly unbelievable . 
but these missteps do not blunt the power of tunney's bravura turn , which carries niagara niagara to a level of poignance it would not have otherwise achieved . 
 ( opens march 20 ) 
 " i didn't know what to expect . 
it's like something you chase for so long , but then you don't know how to react when you get it . 
i still don't know how to react . " 
--michael jordan , on winning his first nba championship in 1991 . . . or , 
my thoughts after meeting him on november 21 , 1997  """

dataneg = 'i hated this movie it was terrible what a disaster i hate it i hate i hate it'
