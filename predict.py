import copy
import numpy as np
import math

class Predict:
	def __init__(self, trainedModel):
		self.trainedModel = trainedModel.tolist()
		
	def multiply(self, list1, list2):
		# Multiply two lists of same size
		result = []
		for i in range(len(list1)):
			if list2[i] != 0:
				result.append(list1[i] * list2[i])
		return result
		
	def multiplyWithInt(self, list, number):
		# Multiply entire list with a given integer
		result = []
		for i in list:
			x = i * number
			result.append(x)
		return result
	
	def getLogList(self, list):
		# Apple log base 2 to all the elements of the list
		for i in range(len(list)):
			try:
				list[i] = math.log2(list[i])
			except:
				print('Zero')
				list[i] = 0
		return list
	
	def addlogCd(self, list):
		# Add log of MLE value to the result list
		for i in range(len(list)):
			list[i] = list[i] + math.log2(self.totalProbList[i])
		return list
	
	def addList(self, list1, list2):
		# Add two list of same size
		result = []
		for i in range(len(list1)):
			result.append(list1[i] + list2[i])
		return result
	
	def getMaxIndex(self, list):
		# Index of maximum value from a list
		max = list[0]
		maxIndex = 1
		for i in range(len(list)):
			if list[i] > max:
				#print('Big')
				maxIndex = i + 1
				max = list[i]
		return maxIndex
	
	def divideWithInt(self, list, number):
		# Function to divide a entire list with an integer
		if number == 0:
			number = 0.0001
		result = []
		for i in list:
			try:
				x = i/number
			except:
				x = 0
			result.append(x)
		return result
		
	def calculateProbList(self, list):
		result = []
		for i in range(1,21):
			result.append(list[i]/list[0])
		return result
		
	def predictOutcome(self, list):
		resultList = []
		for i in range(len(self.trainedModel)):
			# Iterating through the row of test data.
			if list[i] == 0:
				continue

			value = self.trainedModel[i]
			res = self.getLogList(value[1:21])
			if resultList == []:
				resultList = copy.deepcopy(res)
			else:
				res = self.multiplyWithInt(res, list[i])
				resultList = self.addList(resultList, res)
		
		resultList = self.addlogCd(resultList)
		return self.getMaxIndex(resultList)
	
	def predictData(self, data):
		# Entry function
		self.counter = 0
		predictedList = []
		# List consists of pre calculated values of number of records in each class.
		self.classDistribution = [12000, 483, 624, 622, 643, 602, 630, 618, 614, 649, 628, 646, 639, 626, 621, 637, 651, 580, 593, 467, 427]
		print(len(self.trainedModel))
		self.totalProbList = self.calculateProbList(self.classDistribution)
		print(self.totalProbList)
		for index, row in data.iterrows():
			# Iterate through all rows
			rowList = copy.deepcopy(row[1:])
			rowList = rowList.tolist()
			print(index)
			# Passing indvidual rows to predict class
			predictedList.append(self.predictOutcome(rowList))

		return predictedList