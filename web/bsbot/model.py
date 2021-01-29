import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tflearn
import random
import pickle
import json

stemmer = LancasterStemmer()

# restore all of our data structures
data = pickle.load(open("web/bsbot/training_data", "rb"))
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']

# import our chat-bot intents file
with open('web/bsbot/intents.json') as json_data:
    intents = json.load(json_data)

# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')


def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)

    return np.array(bag)


# load our saved model
model.load('web/bsbot/model.tflearn')


ERROR_THRESHOLD = 0.25


def classify(sentence):
    # generate probabilities from the model
    results = model.predict([bow(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i, r] for i, r in enumerate(results) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of intent and probability
    return return_list


def response(sentence, show_details=False):
    results = classify(sentence)
    # if we have a classification then find the matching intent tag
    if results:
        # if the system is not at least 50% sure to have the right answer
        if results[0][1] < 0.5:
            print('Das weiß ich leider nicht! Aber unsere Mitarbeiter Beraten dich gerne! Ruf uns gleich an: 0676/ 123 45 67')
        # loop as long as there are matches to process
        else:
            while results:
                for i in intents['intents']:
                    # find a tag matching the first result
                    if i['tag'] == results[0][0]:
                        # if show details is true, then you see what tag he suspects and how many percent he is sure
                        if show_details:
                            print('tag:', i['tag'])
                        # a random response from the intent
                        return random.choice(i['responses'])

                results.pop(0)
