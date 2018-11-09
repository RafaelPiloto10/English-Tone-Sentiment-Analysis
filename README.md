# Sentiment Analysis Expirement to Predict Tone / Attitude Questions in English
My need to automate and make everything as efficient as possible led to the creation of this program - 

I used TextBlob, a python library that has built in Sentiment Analysis, in the past and
decided to give it a try. 

## Functionality

### Passage Analysis
You can use the expirment Tone Sentiment Analysis, which analyzes a default passeage with answers. You can provide your own passage and answers with the -p and -a

`python3 Tone_Sentiment_Analysis -p {path to txt file} -a "answer,answer,answer"`

### Song Analysis
You can use the Song Sentiment Analysis by simply running the default `GambinoAnalysis.py` python file.
Additional functionality to analyze any song may be added later. 

- Note - matplotlib is a dependency. Install using `pip3 install matplotlib`

## Dependencies
Depending on the file you run, some modules may not be neccessary.
Overall this project uses
* Matplotlib
* TextBlob