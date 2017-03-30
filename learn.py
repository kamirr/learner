#! /usr/bin/python3

# import needed modules
import fileinput
import random
import sys
import os
import re

# generate usable path (/home/<user>/.word-list)
filename = os.path.expanduser('~') + '/.word-list'

# returns number of lines
def countLines(name):
	return sum(1 for line in open(name))

# random index of line in file
def getTarget():
	return random.randint(0, countLines(filename) - 1)

# single question
def quiz():
	# choose random line
	target = getTarget()
	for line in open(filename):
		if target == 0:
			question = line
			break
		target -= 1

	# split it into word and meaning	
	words = question.split(' = ')
	print('>', words[1], end='')

	# read input from user
	for line in sys.stdin:
	# skip new-line char at the end of string
		line = line[:-1]
	# check whether answer is good or not 
		if words[0] == line:
			print('Right!\n')
			break
		else:
			print('\'', line, '\' → \'' + words[0] + '\'', sep='')

# big test
def test():
	# read all the pairs into list
	phrases = []
	for phrase in open(filename):
		phrases.append(phrase.split(' = '))
	
	# shuffle it
	random.shuffle(phrases)
	
	# good answer counter
	count = 0
	for phrase in phrases:
		print('>', phrase[1], end='')
		
		firstTry = True
		for answer in sys.stdin:
			answer = answer[:-1]
			if phrase[0] == answer:
				print('Right!\n')

				# if answer was good in the first time, increment 'count' 
				if firstTry:
					count += 1
				break
			else:
				print('\'', answer, '\' → \'' + phrase[0] + '\'', sep='')
				firstTry = False
	
	# print results of test
	print(count, '/', countLines(filename), " (", int(count / countLines(filename) * 1000) / 10, "%)", sep='')

# check for execution parameters
if len(sys.argv) > 1:
	if sys.argv[1] == 'quiz':
		quiz()
		quit()
	if sys.argv[1] == 'test':
		test()
		quit()

	# if there's no recognizable command 
	with open(filename, 'a') as myfile:
		# check if new phrase is formatted correctly
		pattern = re.compile('.* = .*\Z')
		if pattern.match(sys.argv[1]) == None:
			print('Please, follow \'word = meaning\' rule')
			quit()
	
		# write phrase to file
		myfile.write(sys.argv[1] + '\n')
		quit()

# no extra parameters given – print random phrase
target = getTarget()
for line in open(filename):
	if target == 0:
		print(line, end='')
		break
	target -= 1
