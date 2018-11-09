from textblob import TextBlob
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import time

start = time.time()
print(plt.style.available)
plt.style.use("seaborn-talk") # _classic_test, fivethirtyeight, classic, bmh, seaborn-talk

loc = plticker.MultipleLocator(base=.3)

polarity = []
subjectivity = []

lines = []
polarityEqualsZero = 0

with open("./GambinoSong.txt") as f:
  for line in f.read().split("\n"):
    if line != "" and line not in lines:
      sentiment = TextBlob(line)
      if sentiment.sentiment.polarity != 0:
        polarity.append(sentiment.sentiment.polarity)
      else:
        polarityEqualsZero += 1
        polarity.append(sentiment.sentiment.polarity)
      subjectivity.append(sentiment.subjectivity)
      lines.append(line)
      
def plot(p, data, label, fontsize=12):
     p.plot(data)
     p.locator_params(nbins=3)
     p.set_xlabel("LINES", fontsize=fontsize)
     p.set_ylabel(label, fontsize=fontsize)

fig, sub = plt.subplots(2, 1, constrained_layout=True)
fig.suptitle("Sentiment Analyisis of 'This is America'")

sub[0].axis([0, len(polarity), -1.0, 1.0])
plot(sub[0], polarity, "POLARITY (-1, 1)")
sub[0].yaxis.set_major_locator(loc)
sub[0].xaxis.set_major_locator(plticker.MultipleLocator(base=5))


plot(sub[1], subjectivity, "SUBJECTIVITY (0 -1)")
sub[1].xaxis.set_major_locator(plticker.MultipleLocator(base=5))

# plt.savefig("analysis.png")
print("""
Completed in {:.02f}s. Total lines analyzed: {}.
Lines with canceling polarity: {}.
Total lines with polarity: {}.""".format(time.time() - start, len(set(lines)), polarityEqualsZero, len(set(lines)) - polarityEqualsZero))

plt.show()