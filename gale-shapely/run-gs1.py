#!/bin/bash
# Script name: run-gs1
# Purpose: Run program gs1 (Gale-Shapley) with different input sizes,
# Purpose:	time the execution and record in file data.txt;
# Purpose:	then fit a model for the execution time and 
# Purpose:	report fit stats and a plot of data vs model
# Input: No input required
# Output: A window with the gnuplot graph fitting the model given in file model.gpt,
# Output: also, the statistics of the fit are displayed on stdout,
# Output: also data.txt is created, used, and later removed.
# Requirements: gs1.c must be compiled and the object must reside in
# Requirements: the same directory as this script.
# Requirements: File model.gpt should be created previously with 
# Requirements: the gnuplot code defining the model, requesting
# Requirements: the fit and the plot.
# Requirements: The model should also reside in the same directory.
# Requirements: gnuplot 4.6 should be installed previously.
# Requirements: If a file data.txt exists it must have been generated by this script.

# Run gs1 and create (or append to) data.txt
# Successive runs data accumulate in data.txt

# Fit model, display results and plot graph
import os
import subprocess


f=open('data.txt','w')

for i in range (1000,2000,500):
	
	proc = subprocess.Popen(('python3 gs1.py {}'.format(i)),stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell= True, universal_newlines=True)
 

os.system('gnuplot --persist model.gpt')
