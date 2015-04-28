import wikipedia
from speech import getPhrase

def search():
	search_str = getPhrase()
	search_list = wikipedia.search(search_str)
	if search_str == False:
		return "Sorry, I could not understand what you said!"
	if search_str.lower() == "quit":
		return False
	try:
		return wikipedia.summary(search_list[0], sentences = 2)
	except:
		return "Sorry, I couldn't find anything in wikipedia on " + search_str