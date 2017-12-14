
# coding: utf-8

# # Language Identification (AF/DE/EN/NL)
# 
# This program is designed to take sentences in one of four languages (Afrikaans, German, English, or Dutch) and identify which language it is.
# 
# To do so, I used a multiclass support vector machine. I trained it with 45 sentences from Wikipedia of each language and tested it with 5 sentences from each language. The program got 100% on the test data. I then tested it again with "Blinkenlights" in German and English, getting 75% accuracy from German and 100% accuracy with English.
# 
# To process the data into usable forms, I used regular expressions to take out footnotes/citations. I then used a function to break it into lines on periods and a following space (to eliminate making newlines from decimal points/etc).
# 
# I used a function to break each file's text into lines I could use in the program.
# I then used a function that takes each line from each of the files lines and created a dictionary vector of their bigrams  (e.g. "this sentence" --> 'th', 'hi', 'is', 's ', etc) with binary features (meaning if a bigram occurs more than once, it only inputs one instead of inputting as many as exist).
# I used the DictVectorizer from sklearn.feature_extraction to make it into a more processable form for the SVM.
# I assigned the output to a variable (X) and I also assigned the correct classes to a variable (y). I then trained the SVM with these sets of classes and features.
# 
# I then used the same process to turn the test data into processable form (without the training part).
# I tested the test data by running a loop where it guessed the class and compared it to the correct class. It output which class it guessed and showed the correct class.
# It then added up the correct results and the incorrect results.
# 
# I got 100% accuracy on the test data, then tested "Blinkenlights" (German), "Blinkenlights" (English), and "Uncleftish Beholding" (Anglish -- a form of English where all non-Germanic words are taken out and compound words created with rules similar to German's -- this was just for fun to see what it would classify as). I got 75% accuracy on "Blinkenlights" (German), 100% on "Blinkenlights" (English), and classified "Uncleftish Beholding" as English (as expected).
# 
# The results of this test showed excellent training given the excellent results of the test data.

# In[13]:


#Imports SVM and dictionary vectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn import svm 

#Turns file of lines to list of lines
def linefier(file, tt):
    lines = []
    #Takes a file and turns it into list of lines
    for files in file:
        lines += [line.strip() for line in open(files + tt + '.txt', encoding='utf8')]
    #Removes empty strings in the list
    while '' in lines:
        lines.remove('')
    return lines

#Turns list of lines into feature vectors and classes
def featurefier(lines):
    #Creates a list of classes, correlated to the vectors
    corrects = [line[0] for line in lines]
    #Initializes vector list
    features = [] 
    #Creates features vector
    for line in lines:
        zipped = []
        #Creates bigrams
        for letter in range(len(line) - 3):
            zipped += zip(line[letter + 2],line[letter + 3])
        #Creates the feature vector of bigrams
        features += [{p + q : 1 for p,q in zipped}]
    #Returns list of classes and feature vectors
    return corrects, features
   
#Creates lines, then features of each training file
lines = linefier(["en","de","af","nl"], "_train")
features = featurefier(lines)

#Vectorizes the dictionary vector and assigns it to X
vectorizer = DictVectorizer(sparse = True)
X = vectorizer.fit_transform(features[1])

#Assigns classes to y
y = features[0]

#Initializes classifier and trains classifier with X and y
classifier = svm.LinearSVC()
classifier.fit(X, y)

#Creates lines, then features of each test file
lines = linefier(["en","de","af","nl"], "_test")
features = featurefier(lines)

#Initializes correct and incorrect scores
cor = 0
inc = 0

#Classifies test files
for i in range(len(features[1])):
    #Guesses the class of the feature
    guessed = classifier.predict(vectorizer.transform(features[1][i]))
    #If correct, increase correct score; if incorrect, increase incorrect score
    if guessed == features[0][i]:
        cor += 1
    else:
        inc += 1
    print(guessed, features[0][i])

#Prints scores and accuracy
print("CORRECT: ", cor)
print("INCORRECT: ", inc)
print("ACCURACY: ", cor/(cor + inc))


# In[12]:


#Creates lines, then features of each test file
lines = linefier(["blinkenlights"], "")
features = featurefier(lines)

#Initializes correct and incorrect scores
cor = 0
inc = 0

#Classifies test files
for i in range(len(features[1])):
    #Guesses the class of the feature
    guessed = classifier.predict(vectorizer.transform(features[1][i]))
    #If correct, increase correct score; if incorrect, increase incorrect score
    if guessed == features[0][i]:
        cor += 1
    else:
        inc += 1
    print(guessed, features[0][i])

#Prints scores and accuracy
print("CORRECT: ", cor)
print("INCORRECT: ", inc)
print("ACCURACY: ", cor/(cor + inc))


# In[11]:


#Creates lines, then features of each test file
lines = linefier(["bl"], "")
features = featurefier(lines)

#Initializes correct and incorrect scores
cor = 0
inc = 0

#Classifies test files
for i in range(len(features[1])):
    #Guesses the class of the feature
    guessed = classifier.predict(vectorizer.transform(features[1][i]))
    #If correct, increase correct score; if incorrect, increase incorrect score
    if guessed == features[0][i]:
        cor += 1
    else:
        inc += 1
    print(guessed, features[0][i])

#Prints scores and accuracy
print("CORRECT: ", cor)
print("INCORRECT: ", inc)
print("ACCURACY: ", cor/(cor + inc))


# In[16]:


#Creates lines, then features of each test file
lines = linefier(["an"], "")
features = featurefier(lines)

#Initializes correct and incorrect scores
cor = 0
inc = 0

#Classifies test files
for i in range(len(features[1])):
    #Guesses the class of the feature
    guessed = classifier.predict(vectorizer.transform(features[1][i]))
    #If correct, increase correct score; if incorrect, increase incorrect score
    if guessed == features[0][i]:
        cor += 1
    else:
        inc += 1
    print(guessed, features[0][i])

#Prints scores and accuracy
print("CORRECT: ", cor)
print("INCORRECT: ", inc)
print("ACCURACY: ", cor/(cor + inc))

