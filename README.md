#Decision tree classifier and Confusion Matrix feature program#

##Dependecies:
	numpy - sudo apt-get install python-numpy
	scikit-learn - sudo pip install -U scikit-learn
	** For more help on installation
	   consult http://scikit-learn.org/stable/install.html **

##TO RUN:
	./run.sh
##Features:
	Allows you to do the following:
		*Load an existing tree created from the program;
		 or learn a tree from a comma seperated file (.csv)
		*Test the given accurracy for a tree; outputing a 
		 confusion matrix.
		*Apply a new case to the tree. The program will give
		 you a set a variables to set, afterwards, will ask
		 if you wish to enter another entry or to quit. This
		sets values based on the decision tree.
	
###########    Intructions and Troubleshooting   ############

	When referencing a tree or file, be sure to enter the FULL path 
	of the file if you are *not* in the same directory as said
	file.	
	
## How to learn a new tree
	-When prompted to enter a training set, you will enter a file
	 with a (.csv) extension.
	-Tree will be saved as a file (simply the name of the (.csv) file
	-The tree is now loaded into the program's memory
 
## How to load a tree
	-If you already created a tree with this program (or another like it)
	 simply enter the name of the tree file *(NO .csv)*
	-You will then be notified the tree has been loaded.

##########  REQUIRES A LOADED TREE ############

## How to teest accurracy
	-When prompted, enter the (.csv) file you wish to compare the tree
	 against  
	-You will then be shown a confusion matrix for the results of the test

## Entering new attributes:
	-When prompt, enter the value for each of the variables given.
	-When finished, the program will inform you that if has added the entry
	 if no problems occurred.
