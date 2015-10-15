Readme File

Fuzzer Project Part 2 10/14/2015

Description
- The fuzzer application is a tool that is used to find potential weaknesses in a program. This is done by searching the
 surface of the program, and in this case a particular vulnerable web application.

Running the fuzzer

NOTE * Lab machines can run Python 2.7 by going to the C:/Anaconda directory and running the command:

	python

END NOTE*

- The requirements for the fuzzer are as follows:
	- (provided) The fuzzer itself
	- (provided) File to check for different pages
	- (available) SE Department machine with Python installed 

- In the associated .zip file, you will find the above provided files, as well as the requests library for Python. 

Step 1 - Run python 2.7.x in the command line (*Note: If you have multiple instances of python, you will need to make
sure you are running 2.7.x, and not 3+, as there will be errors when doing so)

	Example, in a lab machine, you are able to do so running the following command in the C:\Anaconda directory:
	
	python

Step 2 - Once you have python running, locate the fuzzer.py file given and copy the url

	Example, the location of the file is C:\Users\rnn7726\PycharmProjects\Fuzzer\Fuzzer.py
	
Step 3 - Add in an additional \ character where they appear in the url
	
	Example, the above becomes C:\\Users\\rnn7726\\PycharmProjects\\Fuzzer\\Fuzzer.py
	
Step 4 - Run the execfile('url') command, where url is the modified url from step 3

	Example, execfile('C:\\Users\\rnn7726\\PycharmProjects\\Fuzzer\\Fuzzer.py')

This will run the fuzzer and you will be able to execute commands within it. For this first part of the project, you
will be able to use the discover command alongside two different options, --custom-auth= and --common-words=, according
to the specifications set within the project description.

Risks:
Some risks with the project include incomplete functionality within the application using certain test functions.
Please see the Fuzzer.py document for comments regarding specific test functionality on delayed responses and HTTP
Requests