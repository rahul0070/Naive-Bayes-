from algorithm import Naive
import pandas as pd
import numpy as np
from playsound import playsound
from collections import Counter
import math


def toFile(predictedList, size):
	#Function to write to file.
	index = size
	row = []
	for i in predictedList:
		row.append([index, i])
		index += 1
		
	finalOutput = pd.DataFrame(data = row, columns = ['id', 'class'])
	finalOutput.to_csv('data/predictedc.csv', index=False)

def loadData(filename):
	# Function to load CSV file
	try:
		print('Loading Data.')
		data = pd.read_csv(filename, index_col = False, header = None)
		playsound('data/beep2.mp3')
		print('Done.')
	except:
		print('ERROR. CSV file not found.')

	return data

	
def confusion(data):		
	size = (3 * data.shape[0])//4
	data = data.iloc[:size, :]
	inp = input(data.shape)
	model.train(data, trainedData)
	
def makeConfusion(data):
	# Function to train 3/4th of the data
	size = (3 * data.shape[0])//4	
	data = data.iloc[size:, :-1]
	predicted = model.predict(trainedData, data)
	toFile(predicted, size)
		

def train(data):	
	# Function to train full data
	model.train(data, trainedData)
	
def predictFull(data):
	# Function to predict test data
	predicted = model.predict(trainedData, testData)
	toFile(predicted, 12001)

if __name__ == '__main__':
	training = 'data/training.csv'
	testing = 'data/testing.csv'
	sampleTest = 'sample/sampleTesting.csv'
	sampleTrain = 'sample/sampleTraining.csv'
	trainedFile = 'data/trained.npy'

	inp = input('Enter an option (1. Train, 2. Predict, 3. Make confusion training model ): ')
	inp = int(inp)

	model = Naive()  
	try:
		print('Loading trained data...')
		trainedData = np.load(trainedFile, allow_pickle = True)
		flag = 1
		print('Done.')
	except:
		print('NO EXISTING TRAINED DATA. CREATING NEW MODEL...')
		trainedData = []
		flag = 0

	if inp == 1:
		data = loadData(training)
		train(data)

	elif inp == 2:
		data = loadData(testing)
		predictFull(data)

	elif inp == 3:
		data = loadData(training)
		confusion(data)
		makeConfusion(data)

	playsound('data/beep.mp3')