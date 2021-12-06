from string import punctuation
from os import listdir
from numpy import array
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from nltk.corpus import stopwords
import string


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
	model = load_model("FLOWER/latest_model.h5")
	model.summary()
	sequenced_data = handle_data(data)
	
	#make prediction from data
	predictions = model.predict(sequenced_data, verbose = 0)
	if predictions > 0.5: 
		print(predictions, ' data is positive')
		return predictions.tolist(), 'data is positive'
	else:
		print(predictions,' data is negative')
		return predictions.tolist(), 'data is negative'



