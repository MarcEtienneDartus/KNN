import csv
import math
from operator import itemgetter
from collections import Counter
import os

#CSV file openning
def CsvReader(filename):
    csvData = [] 
    current_folder = os.path.dirname(os.path.abspath(__file__)) #parent folder path
    exact_file_path = os.path.join(current_folder, filename) #add filename in path
    with open(exact_file_path, 'r')  as f: #open file
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            csvData.append(row) #adding value in our array
    return csvData

#calcul for the euclidienne's distance betweeen two plant
def Distance(dataItem,searchItem):
    distance = 0 
    for index in range(min(len(searchItem), len(dataItem))): 
        distance += math.pow(float(dataItem[index])-float(searchItem[index]),2) 
    return math.sqrt(distance) 

#Search nearest neighbors
def SearchNeighbors(dataSet,searchItem,k):
    distanceArray = []
    for itemIndex in range(len(dataSet)): #For each plant
        distance = Distance(dataSet[itemIndex],searchItem)
        if(distance > 0.0): #Check for positive value
            distanceArray.append([distance,dataSet[itemIndex]])
    distanceArray = sorted(distanceArray, key=itemgetter(0)) #sort the array for finding the topest one
    nearestNeighbors = [distanceArray[i][1][-1] for i in range(k)] 
    typeSearchItem = Counter(nearestNeighbors) #count the number or nearest neighbors
    return typeSearchItem.most_common(1)[0][0]

#Search and write result for prediction
def FindValue(trainingSet,predictSet,k):
    dir_path = os.path.dirname(os.path.realpath(__file__)) 
    text_file = open(dir_path+"\\Prediction.txt", "w") 
    for i in range(len(predictSet)):
        searchItem = predictSet[i]
        text_file.write(SearchNeighbors(trainingSet,searchItem,k)+"\n") #write the value found in our result file
    text_file.close()
    print("The prediction is complete, the result is in the Prediction.txt file")

#Evaluation for choosing K
def EvaluateK(dataSet,pourcentageTraining,k):
    trainingSet = dataSet[:int(len(dataSet)*pourcentageTraining)]
    predictSet = dataSet[int(len(dataSet)*pourcentageTraining):]
    goodGuess = 0
    for itemIndex in range(len(predictSet)):
        predictLine = predictSet[itemIndex] #add predict value in the array
        searchItem = predictLine[:len(predictLine)-1]
        realValue = predictLine[-1] #get the real value
        preditedValue = SearchNeighbors(trainingSet,searchItem,k) 
        goodGuess += 1 if realValue == preditedValue else  0 #if prediction is correct
    print("K : "+str(k)+", Percentage of TrainingSet : "+str(pourcentageTraining*100)+"% Percentage of accuracy: " + str(goodGuess/len(predictSet)*100)+"%")


if __name__ == '__main__':
    trainingSet = CsvReader('training.csv')
    for k in range(1,21):
        EvaluateK(trainingSet,0.8,k)
    predictSet = CsvReader('predict.csv')
    FindValue(trainingSet,predictSet,7)
