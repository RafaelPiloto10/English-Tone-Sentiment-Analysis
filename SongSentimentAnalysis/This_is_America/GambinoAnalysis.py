from textblob import TextBlob
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")

polarity = []
subjectivity = []
with open("./GambinoSong.txt") as f:
  [(polarity.append(TextBlob(line).sentiment.polarity), subjectivity.append(TextBlob(line).subjectivity)) for line in f.read().split("\n") if line != "" and TextBlob(line).polarity != 0]

def plot(ax, data, label, fontsize=12, axis=None):
     ax.plot(data)
     ax.locator_params(nbins=3)
     if axis is not None:
       ax.axis(axis)
     ax.set_xlabel("LINES", fontsize=fontsize)
     ax.set_ylabel(label, fontsize=fontsize)

fig, sub = plt.subplots(2, 1, constrained_layout=True)
fig.suptitle("Sentiment Analyisis of 'This is America'")
plot(sub[0], polarity, "POLARITY (-1, 1)", .1)
plot(sub[1], subjectivity, "SUBJECTIVITY (0 -1)")


plt.show()
