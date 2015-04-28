import os
from wikiSearch import search

while True:
	answer = search()
	if answer == False:
		break
	answer = answer.replace('(' , '')
	answer = answer.replace(')', '')
	answer = answer.replace("'", "")
	print answer
	os.system("say " + answer.encode('utf-8'))
