import speech_recognition as sr

def getPhrase():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)

	try:
		return r.recognize(audio)
	except:
		return False