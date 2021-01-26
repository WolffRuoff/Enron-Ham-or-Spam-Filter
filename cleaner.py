#%%
import nltk
import string


#%% Downloading stopwords
nltk.download()
stopwords = nltk.corpus.stopwords.words("english")
stopwords += ["ref", "name"]

#%%
"""
Opens a file, splits it, strips of punctuation, makes text lowercase, removes any stopwords, and the converts numbers to "number"

@author Ethan Ruoff
@see filter.py
@see learn.py
@return {list} A sanitized list
"""
def getCleanText(folder, typ, filename):
    f = open("..\\HW5\\" + folder + "\\" + typ + "\\" + str(filename), errors="ignore")
    text = f.read()

    text = text.split()
    text = [w.strip(string.punctuation) for w in text]

    text = [i.lower() for i in text if i not in stopwords]
    cleanList = []
    for w in text:
        if w.isnumeric() == True:
            cleanList.append("number")
        else:
            cleanList.append(w)
    
    f.close()
    return cleanList
# %%
