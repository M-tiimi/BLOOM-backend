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

datapos2 = """plot : a dude and his brother are driving cross-country and decide to fool around with a trucker on their cb radio . 
it isn't long before their little prank gets someone put into a coma ( long story ) and the next thing you know , the trucker is following them too . 
lotsa nuttiness ensues and then , they pick up their other friend , venna , a girl who the dude has a crush on . 
but what's this . . . ? 
the trucker is still on their tail and is now harassing all three of the young whippersnappers . . . ? 
you bet ! 
buckle up , dorothy . . . this is gonna be one bumpy ride ! 
critique : a good ol' time at the movies ! 
here's a film that actually gives away most of its plotline in its trailer and doesn't really bring anything " new " to the forefront ( if you've seen flicks like duel and breakdown , you've crossed this path before ) , but still manages to entertain you gangbusters , with realistic situations , believable characters , funny moments , thrills , chills , the whole shebang . 
let's give it up for director john dahl , who continues to put out solid films every other year ( if you haven't seen red rock west , do yourself a favor right now , and jot it down on a piece of paper and rent it at your earliest convenience ) . 
and much like that film , this one has an excellent premise and sets everything up at an even pace . 
it gives you a little bit of background on each of the main three characters , and then shows you how one small prank , can lead to a whole lotta trouble for everyone ! 
paul walker really surprised me in this movie , since i've never much thought of him as anything more than a pretty face ( and damn , is it ever pretty or what ? ! ) 
but here , he actually manages to put some depth behind the looks and that's always appreciated in films in which you are so closely tied to the main characters . 
sobieski is also good , but she isn't in the movie for as long as you'd think , but the man who really takes this film to another level , is steve zahn . 
if you've loved this guy as the " goofball " in most of his previous roles , you'll appreciate him even more here , as the dude who starts off as one of the most manic and excited human beings i've seen in quite some time ( " this is so awesome ! ! " ) , 
only to turn into a man scared out of his wits by the end of the flick . 
and speaking of the ending , boy , does this movie deliver some chilling moments during its final 15 clicks or what ? ! ? 
the arrow and i were practically in each others arms ( well , maybe i'm exaggerating , but you catch my drift ) as each minute brought about another turn of events which in turn , took it all to an even higher level . 
once again , kudos to director dahl for being able to generate that type of intensity , suspense and tension , with a great score , editing , style and camerawork . 
plot-wise , i too did wonder how the " bad guy " was able to track them so well , but it didn't really bother me all that much ( you can assume that he had bugged their car ? ) . 
but pretty much everything else in the story stuck like glue and i couldn't help but put myself in their shoes and appreciate their thoroughly desperate circumstance . 
a great movie with an even cooler ending , this film will likely be remembered as one of the better thrillers of the year . 
 " this is amazing ! ! ! " 
where's joblo coming from ? 
american psycho ( 10/10 ) - deep blue sea ( 8/10 ) - eye of the beholder ( 4/10 ) - the fast and the furious ( 7/10 ) - final destination ( 8/10 ) - the glass house ( 6/10 ) - no way out ( 8/10 )  """

dataneg = 'i hated this movie it was terrible what a disaster i hate it i hate i hate it'
