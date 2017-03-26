# Mathew Jackson -
# Project 2 - Machine Learning Software
# Artifical Intelligence and Heuristics
# Wrapper script for scikit-learn

# !ATTENTION! #
# For help or troubleshoot, see README first. Otherwise
# feel free to contact me at mcj16@zips.uakron.edu

# Libraries for learning and tree struct etc
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
import numpy as nump
import csv
import pickle
import os
# Sub-utility to extract data from the csv files
def extractFromCSV(inpFile):
    print("Retrieving Data...")
    try:
        with open(inpFile) as file:
            file = csv.reader(file)
            temp = next(file)

            targetNames = int(temp[0])
            featureNames = int(temp[1])
            target_names = nump.array(temp[2:])
            data = nump.empty((targetNames, featureNames))
            target = nump.empty((targetNames,), dtype=nump.int)
            temp = next(file)
            featureNames = nump.array(temp[:-1])
            # Find each data piece and extract it to arrays
            for i, itr in enumerate(file):
                data[i] = nump.asarray(itr[:-1], dtype=nump.float64)
                target[i] = nump.asarray(itr[-1], dtype=nump.int)

            print("Data retrieval successful...")
            return data,target, featureNames, target_names
    except:
        print("ERROR: Problem in extractFromCSV()")


# Sub utility to save the tree as file -- will create 3 files in directory
def saveTreeFile(tree, featureNames, target_names, file):
    try:
        print("Saving Tree...")
        file = str(file)[:-4]
        pickle.dump(tree, open(file, "wb"))
        print("The tree saved as: " + file)
        featureNames = file + "_fattr"
        pickle.dump(featureNames, open(featureNames, "wb"))
        targetNames = file + "_tattr"
        pickle.dump(target_names, open(targetNames, "wb"))
        print("Utility files generated")
        return
    except:
        print("ERROR: Problem in saveTreeFile()")
##################################################### MAIN #############################################################
print("\n\t\t\tWelcome to Machine Learning ")
print("\t\t\tDecision Tree Edition")
print("\t\t\tVersion 1.0 \n\n")
# This variable determines if a tree is loaded, as well
# Will not allow you to use option 2 or 3 without it being NOT 0
loadedTree = 0
# Main Loop
while True:
    if loadedTree == 0:
        print("Currently: NO TREE LOADED")
    else:
        print("Currently: TREE LOADED")
    mainOptions = int(input("Select an option:\n 1. Load/Learn a decision tree \n 2. Test Accuracy of loaded decision tree"
                        "\n 3. Apply the decision tree to new cases \n 4. Exit \n"))

    if mainOptions in [1,2,3,4]:
        if mainOptions == 1:
            while True:
                learn_load = int(input("Choose sub-option: \n 1 Learn Tree\n 2 Load Tree\n"))
                if learn_load in [1, 2]:
                    print("Working...")
                    break
                else:
                    print("Invalid input. Try again")
            # Learning a tree
            if learn_load == 1:
                file = raw_input("Enter a training-set file path:\n ")
                data, target, featureNames, target_names = extractFromCSV(file);
                #print("Made it here")
                loadedTree = DecisionTreeClassifier()
                loadedTree = loadedTree.fit(data, target)
                saveTreeFile(loadedTree, featureNames, target_names, file)

            # Load a tree
            else:
                try:
                    file = raw_input("Enter a tree to load: ")
                    loadedTree = pickle.load(open(file, "rb"))
                    featureAttr = file + "_fattr"
                    featureNames = pickle.load(open(featureAttr, "rb"))
                    targetAttr = file + "_tattr"
                    target_names = pickle.load(open(targetAttr, "rb"))
                except:
                    print("File Load Error! \nTry Again")
                    continue;
                print("Loading Completed")
        # Requires a tree to be loaded
        elif (mainOptions == 2 and loadedTree != 0):
            test = raw_input("Enter testing data set (<file>.csv): ")
            data, target, featureNames, target_names = extractFromCSV(test)
            true_values = target
            pred_values = loadedTree.predict(data)

            print("RESULTS: ")
            print("Output of confusion matrix: ")
            print(confusion_matrix(true_values, pred_values))
        # Requires a tree to be loaded
        elif (mainOptions == 3 and loadedTree != 0):
            while True:
                attributes = []
                print("\nNew Attribute: ")
                for i in featureNames:
                    try:
                        attributes.append(float(input(i + ": "))).reshape(1, -1)
                    except:
                        print("\nEnter value: ")
                t = loadedTree.predict(attributes)

                out = target_names[t].reshape(1, -1)

                print("Output: " + str(out))
                #TODO: error handling
                if raw_input("Insert another case? (Y/n) ").lower() == "y":
                    continue
                else:
                    break
        elif mainOptions == 4:
            print("\n\nTerminating Program")
            print("I hope you've LEARNED something!")
            break
        else:
            print("Please learn a tree or load an existing tree")
            continue
    else:
        print("!Incorrect input. Try again!")
        continue
