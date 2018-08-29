import textblob
from textblob.sentiments import NaiveBayesAnalyzer

passage1 = open("passage01.txt", "r").read()
passage2 = open("passage02.txt", "r").read()

passage1_answers = ["Evenhanded and logical",
           "Whimsical and poetic",
           "Imprecise and accusative",
           "Sarcastic and biting",
           "Paranoid and skeptical"]

passage2_answers = ["He was sardonic",
                    "He was apathetic",
                    "He was offended",
                    "He was critical",
                    "He was earnest"]

def evaluatePassage(passage, answers):

	blob = textblob.TextBlob(passage)
	blob_answers = [textblob.TextBlob(x) for x in answers]
	sent = blob.sentiment

	print("Passage possible Tone answers:")

	lowest = None
	greatest = None

	for answer in blob_answers:
		print("{} - {}".format(answer, answer.sentiment))
		if greatest and sent.polarity < answer.sentiment.polarity < greatest.sentiment.polarity:
			greatest = answer
		elif answer.sentiment.polarity > sent.polarity:
			greatest = answer
		if lowest and sent.polarity > answer.sentiment.polarity > lowest.sentiment.polarity:
			lowest = answer
		elif answer.sentiment.polarity < sent.polarity:
			lowest = answer
		
	print("Passage has a sentiment polarity of: {} ".format(sent), end="\n\n")
	print("The Analysis best calculates '{}' and '{}' to be the best possible answers".format(lowest, greatest), end = "\n\n")

evaluatePassage(passage1, passage1_answers)

