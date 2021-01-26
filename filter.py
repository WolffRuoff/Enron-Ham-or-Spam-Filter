#%% Imports
import json
import os
import cleaner
import math
#%%
dic = {}
probs = {'ham': {}, 'spam': {}}
v = 0

"""
Calculates V and the calls printPredictions() for two testing folders

@author Ethan Ruoff
@see printPredictions()
@see knowledge.json
"""
def main():
    global dic
    global v

    with open("knowledge.json") as hamandspam:
        dic = json.load(hamandspam)

    #Calculate V
    uniqueKeys = list(dic["ham"].keys())
    uniqueKeys = uniqueKeys + [i for i in dic["spam"].keys() if i not in uniqueKeys]
    v = len(uniqueKeys)
    
    print("Enron2 Folder Results:")
    printPredictions("enron2")

    print("\nEnron3 Folder Results:")
    printPredictions("enron3")


"""
Runs hamorspam() for every file in the @param, prints results, and calculates the accuracy, precision, and recall

@param {string} folder First folder name enron2 | enron3

@see hamorspam()
"""
def printPredictions(folder):
    kinds = ["spam", "ham"]
    
    truePos = 0
    falsePos = 0
    trueNeg = 0
    falseNeg = 0

    #For every file in the ham and spam folders, predict if they're ham or spam
    for kind in kinds:
        for files in os.listdir(os.path.join("..","HW5", folder, kind)):
            result = hamorspam(folder, kind, files)
            if result == "truePositive":
                truePos += 1
            elif result == "falsePositive":
                falsePos += 1
            elif result == "trueNegative":
                trueNeg += 1
            else:
                falseNeg += 1
    print('True Positive: %d' % truePos)
    print('False Positive: %d' % falsePos)
    print('True Negative: %d' % trueNeg)
    print('False Negative: %d' % falseNeg)
    
    accuracy = (truePos + trueNeg) / (truePos + trueNeg + falsePos + falseNeg) 
    print('\nAccuracy: %.2f' % accuracy)

    precision = truePos / (truePos + falsePos)
    print('Precision: %.2f' % precision)

    recall = truePos / (truePos + falseNeg)
    print('Recall: %.2f' % recall)


"""
Determines if a file is ham or spam
@param {string} folder First folder name enron2 | enron3
@param {string} folder2 Folder that determines type of file ham | spam
@param {string} textFile the file being judged

@return {string} The result of the test
@see predictProb()
"""
def hamorspam(folder, folder2, textFile):
    #sanitize the text file into a list
    words = cleaner.getCleanText(folder, folder2, textFile)

    #Get the probability of ham and spam
    hamProb = predictProb("ham", words)
    spamProb = predictProb("spam", words)
    #print('Ham = ' + str(hamProb) + ' Spam = ' + str(spamProb))

    if spamProb > hamProb:
        if folder2 == "spam":
            return "truePositive"
        else:
            return "falsePositive"
    else:
        if folder2 == "ham":
            return "trueNegative"
        else:
            return "falseNegative"


"""
Calculates the logarithmic probability of the words being ham or spam

@param {string} kind String specifying if you're looking for the probability of ham or spam
@param {list of strings} words List of words from the text file

@return {number} The logarithmic probability of words being kind
@see getProb()
"""
def predictProb(kind, words):
    global probs
    wordsProb = []


    for w in words:    
        #If probability not already calculated, calculate it
        if w not in probs[kind].keys():
            probs[kind][w] = getProb(w, words, kind)

        #Add the probability to the word-by-word list for the text file's probabilities
        wordsProb.append(probs[kind][w])
    
    #Get the logs of the probabilities to avoid small numbers
    logProbs = sum([math.log(i) for i in wordsProb])
    #print('Log %.3f' % logProbs)
    
    #Probability numbers found in summary.txt of enron1 folder
    if kind == "spam":
        probability = 1500 / (1500 + 3672)
    else:
        probability = 3672 / (1500 + 3672)  
    
    #alternate way to calculate probability
    #probability = len(dic[kind].keys()) / (len(dic["spam"].keys()) + len(dic["ham"].keys()))

    finalProb = math.log(probability) + logProbs
    return finalProb

"""
Calculates the probability for the word specified

@param {string} w The word that needs a probability calculated
@param {list} words The list of words in the text file
@param {string} kind Specifying if you're looking for ham or spam probability
@return {number} Probability of w appearing in kind
"""
def getProb(w, words, kind):
    countWC = dic[kind].get(w, 0)
    countC = sum(dic[kind].values())
    return (countWC+1)/(countC + v)

main()# %%

# %%
