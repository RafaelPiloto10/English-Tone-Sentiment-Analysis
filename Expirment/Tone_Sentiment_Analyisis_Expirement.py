"""
	Created by: Rafael Piloto 8.29.2018
	
	Sentiment Analyisis Experiement
		- I wanted to create a program that will try to predict the answer to Tone / Attitude English Questions
		  using sentiment Analysis
	Uses TextBlob

"""


import textblob
from textblob.sentiments import NaiveBayesAnalyzer # Optional - UNUSED

# Open passages

passage1 = open("passage01.txt", "r").read() 
passage2 = open("passage02.txt", "r").read()

# Answers to the first passage from College Board AP English Exam
passage1_answers = ["Evenhanded and logical",
           "Whimsical and poetic",
           "Imprecise and accusative",
           "Sarcastic and biting",
           "Paranoid and skeptical"]
# Answers to the second passage from College Board AP English Exam
passage2_answers = ["He was sardonic",
                    "He was apathetic",
                    "He was offended",
                    "He was critical",
                    "He was earnest"]

def evaluatePassage(passage, answers):
	# Function that will preform sentiment analysis on a passage & its answers
	# Calculates 2 possible answers whose sentiment polarity closely relates to that of the passage
	blob = textblob.TextBlob(passage) # Passage
	blob_answers = [textblob.TextBlob(x) for x in answers] # Answers
	sent = blob.sentiment # Passage Sentiment

	print("Passage possible Tone answers:")

	lowest = None
	greatest = None

	for answer in blob_answers:
		print("{} - {}".format(answer, answer.sentiment))
		if greatest and sent.polarity < answer.sentiment.polarity < greatest.sentiment.polarity:
			# If the polarity is greater than the passage but less than all the other polarities
			greatest = answer
		elif answer.sentiment.polarity > sent.polarity:
			greatest = answer # No other answer previously recorded. Set the first greatest one
		if lowest and sent.polarity > answer.sentiment.polarity > lowest.sentiment.polarity:
			# If the polarity is lower than the passage but less than all the other polarities
			lowest = answer
		elif answer.sentiment.polarity < sent.polarity:
			lowest = answer # No other answer previously recorded. Set the first lowest one
		
	print("Passage has a sentiment polarity of: {} ".format(sent), end="\n\n")
	print("The Analysis best calculates '{}' and '{}' to be the best possible answers".format(lowest, greatest), end = "\n\n")

evaluatePassage(passage1, passage1_answers) # Adjust based on passage and answers

