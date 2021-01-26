#%% Imports
import re, os
import json
import cleaner


#%% 
"""
Creates a bag-of-words json titled "knowledge.json" that contains word frequencies for both ham and spam folders

@author Ethan Ruoff
@see cleaner.py
"""
def main():
    hamandspam = {}
    
    hamDict = {}
    for files in os.listdir(os.path.join("..","HW5", "enron1", "ham")):
        words = cleaner.getCleanText("enron1", "ham", files)
        #For each word in the text file
        for w in words:
            #If the words not in the dictionary create and assign value 1 
            if w not in hamDict.keys():
                hamDict[w] = 1
            #If the words in it already add 1 to value (number of ocurrences)
            else:
                hamDict[w] += 1

    spamDict = {}
    for files in os.listdir(os.path.join("..", "HW5", "enron1", "spam")):
        words = cleaner.getCleanText("enron1", "spam", files)
        for w in words:
            if w not in spamDict.keys():
                spamDict[w] = 1
            else:
                spamDict[w] += 1

    #Creates a nested dictionary so that the dump is easier
    hamandspam["ham"] = hamDict
    hamandspam["spam"] = spamDict

    with open("knowledge.json", "w") as dadumped:  
        json.dump(hamandspam, dadumped)

# Function to print the tree in a readable manner
# Credit: HW assignment I did for a class while I was abroad
def print_dict_tree(d, indent=0):
    for key, value in d.items():
        print('    ' * indent + str(key), end=' ')
        if isinstance(value, dict):
            print(); print_dict_tree(value, indent+1)
        else:
            print(":", value)
# %%
main()
# %%
