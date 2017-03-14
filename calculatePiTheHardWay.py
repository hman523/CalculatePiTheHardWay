#################################################
#Author: Stephen Hunter Barbella (AKA hman523)  #
#Date: 3/14/2017 (Pi day )						#
#This program is released under GPL v. 3		#
#It is provided AS IS and comes with no warrenty#
#Purpose: Calculate pi in a strange way 		#
#Inspired by standupmath's youtube video and	#
#http://www.cut-the-knot.org/ 's proof			#
#################################################

#Imports
from math import sqrt
from math import gcd
from random import randint
import sys

max = sys.maxsize

#Method to find if two values are coprime
def isCoprime(a, b):
    return gcd(a, b) == 1


#Main method
if __name__ == '__main__':
	while(True):
		while(True):
			print("How many iterations")
			userInput = input()
			try:
				userInput = int(userInput)
				break
			except:
				print("Whoops")
		count = 0
		coprimeCount = 0
		while(count < userInput):
			int1 = randint(1, max)
			int2 = randint(1, max)
			if(isCoprime(int1,int2)):
				coprimeCount = coprimeCount + 1
			count = count + 1
		prb = coprimeCount/count
		if (prb is 0):
			print("Not enough iterations for anything to work.")
		else:
			pi = sqrt(6/prb)
			print(pi)

		

			
