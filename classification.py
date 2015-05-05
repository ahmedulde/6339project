
#Ahmed Ulde (1001090889)
#ref http://machinelearningmastery.com/naive-bayes-classifier-scratch-python/

import csv
import math
import collections
import pandas
import time
def calculateProbability(x, mean, stdev):
	try:
		exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
		return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent
	except ZeroDivisionError:
		return 1
		
def summarizeByClass(separated,list):
	summaries={}
	for i in list:
		d=separated.get_group(i).describe()#
		summary={}
		for cols in d:
			mean=d[cols]['mean']
			std=d[cols]['std']
			summary[cols]=[mean,std]
		summaries[i]=summary
	return summaries
	
def calclassprobabilities(summaries,testrow):
	probabilities={}
	for classlabel, dict in summaries.items():
		probabilities[classlabel] = 1
		for term,list in dict.items():
			if term not in ('user_id','avg_stars'):
				mean=list[0]
				std=list[1]
				x=testrow[term]
				probabilities[classlabel] *= calculateProbability(x, mean, std)
	return probabilities
	
def predict(summaries,testrow):
	probabilities=calclassprobabilities(summaries,testrow) 
	max=0
	label=0
	for classval, pro in probabilities.items():
		if(pro>max):
			max=pro
			label=classval
	return label
	
def getPrediction(summaries,testSet):
	predictions=[]
	count=testSet.count()['user_id']
	for i in range(0,count):
		result=predict(summaries,testSet.iloc[i])
		predictions.append(result)	
	return predictions
	
def main():
	csv_reader=pandas.read_csv('xaa.csv')
	data=csv_reader.sort(columns='avg_stars')#sort according to class labels
	#separate data by class
	separated=data.groupby('avg_stars',as_index='true')#get_group
	l=[]
	for i in separated:
		l.append(i[0])
	#get the summary of each group
	summaries=summarizeByClass(separated,l)
	#print(summaries)
	summarybyclass=separated.describe()
	#print(summarybyclass.groups('5'))
	testSet=pandas.read_csv('xab.csv')
	predictions=getPrediction(summaries,testSet)
	print(predictions)
	f=open('userresult.csv','w')
	f.write("user_id,avg_stars\n")
	for i in range(len(predictions)):
		temp=(str(testSet.iloc[i]['user_id'])+","+str(predictions[i])+"\n")
		f.write(temp)
	f.close
	print('Completed!')
main()