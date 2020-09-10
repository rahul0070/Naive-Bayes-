try:
	import pandas as pd
	import numpy as np
	from collections import Counter
	import copy
except:
	x = input('WARNING: Requirements not installed. "pip install -r requirements.txt" to install.')
	

class Naive:
	def __init__(self):
		pass

	def calculateMAP(self, df, composition1):
		# Calculating MAP value for a single column.
		for index, row in df.iterrows():
			if row[0] != 0:
				composition1[row[1]] += 1
			
		for i in range(1,21):
			composition1[i] = (composition1[i] + self.beta)/(self.classTotal[i] + (self.beta * 61189))
			
		return composition1
	
	def traverseColumns(self, data, r1, r2):
		# Calculates the MAP values by iterating through columns in training data.
		for i in range(r1, r2):
			print(i)
			composition = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
			dataTemp = data.iloc[:, [i, -1]]
			dataTemp.columns = ['id', 'Class']
			distribution = self.calculateMAP(dataTemp, composition)
			self.objList.append(distribution)

			
	def predict(self, trainedModel, testData):
		# Function calls predict model to predict a given new test data.
		from predict import Predict
		pr = Predict(trainedModel)
		resultList = pr.predictData(testData)
		return resultList
		
	def train(self, data, trainedData):
		# Entry point.
		self.objList = []
		self.testlist = []
		self.trainingData = data
		self.beta = 0.0001
		startingIndex = 1
		#pre calculated values (number of words in each class.)
		self.classTotal = [0, 154382, 138499, 116141, 103535, 90456, 144656, 64094, 107399, 110928, 124537, 143087, 191242, 97024, 158750, 162521, 236747, 172257, 280067, 172670, 135764]

		#Pre calculated values of number of records/documents in each class.
		self.classDistribution = [12000, 483, 624, 622, 643, 602, 630, 618, 614, 649, 628, 646, 639, 626, 621, 637, 651, 580, 593, 467, 427]
			
		if len(trainedData) != 0:
			startingIndex = len(trainedData)
			self.objList = trainedData.tolist()
		
		self.traverseColumns(data, startingIndex, startingIndex + 10000)

		# Saving result as numpy file.
		array = np.asarray(self.objList)
		np.save('data/trained', array)
		print('Done.')