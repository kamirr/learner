#! /usr/bin/python3

import fileinput
import random
import sys
import os
import re

filename = os.path.expanduser('~') + '/.word-list'

def countLines(name):
	return sum(1 for line in open(name))

def getTarget():
	return random.randint(0, countLines(filename) - 1)

def quiz():
	target = getTarget()
	for line in open(filename):
		if target == 0:
			question = line
			break
		target -= 1
	
	words = question.split(' = ')
	print('>', words[1], end='')

	for line in sys.stdin:
		line = line[:-1]
		if words[0] == line:
			print('Right!')
			break
		else:
			print('\'', line, '\' → \'' + words[0] + '\'', sep='')

def test():
	phrases = []
	for phrase in open(filename):
		phrases.append(phrase.split(' = '))
	
	random.shuffle(phrases)
	
	count = 0
	for phrase in phrases:
		print('>', phrase[1], end='')
		
		firstTry = True
		for answer in sys.stdin:
			answer = answer[:-1]
			if phrase[0] == answer:
				print('Right!\n')
				
				if firstTry:
					count += 1
				break
			else:
				print('\'', answer, '\' → \'' + phrase[0] + '\'', sep='')
				firstTry = False
	
	print(count, '/', countLines(filename), " (", int(count / countLines(filename) * 1000) / 10, "%)", sep='')

if len(sys.argv) == 2:
	if sys.argv[1] == 'quiz':
		quiz()
		quit()
	if sys.argv[1] == 'test':
		test()
		quit()

	with open(filename, 'a') as myfile:
		pattern = re.compile('.* = .*\Z')
		if pattern.match(sys.argv[1]) == None:
			print('Please, follow \'word = meaning\' rule')
			quit()
	
		myfile.write(sys.argv[1] + '\n')
		quit()

target = getTarget()
for line in open(filename):
	if target == 0:
		print(line, end='')
		break
	target -= 1
