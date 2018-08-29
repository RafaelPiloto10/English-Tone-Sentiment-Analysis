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

blob1_answers = [textblob.TextBlob(x) for x in passage1_answers]
blob2_answers = [textblob.TextBlob(x) for x in passage2_answers]

blob1 = textblob.TextBlob(passage1) #, analyzer=NaiveBayesAnalyzer())
blob2 = textblob.TextBlob(passage2)

sent1 = blob1.sentiment
sent2 = blob2.sentiment
print("\nPassage01 :")
for answer in blob1_answers:
    print("{} - {}".format(answer, answer.sentiment))
print("Passage01 has a sentiment polarity of: {} ".format(sent1))

print("\n\nPassage02 :")
for answer in blob2_answers:
    print("{} - {}".format(answer, answer.sentiment))

print("Passage02 has a sentiment polarity of: {} ".format(sent2))


