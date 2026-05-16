#Import Necessary Libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

#Download required NLTK data (only needed once)
nltk.download("vader_lexicon")
nltk.download("stopwords")
nltk.download("punkt")

from nltk.sentiment.vader import SentimentIntensityAnalyzer

#Initialize the sentiment analyzer
sid = SentimentIntensityAnalyzer()

#Sample text for emotion detection
text = """
Life is sad and I want to break it into cards
"""

#Function to detect emotions
def detect_emotion(text):
	#Analyze Sentiment
	scores = sid.polarity_scores(text)

	#Display Sentiment Scores
	print("Sentiment Scores:", scores)

	#Determine emotion based on scores
	if scores["compound"] >= 0.5:
		emotion = "Joy"
	elif scores["compound"] <= -0.5:
		emotion = "Sadness"
	elif scores["neg"] > 0.5:
		emotion = "Anger"
	elif scores["neu"] > 0.7:
		emotion = "Neutral"
	else:
		emotion = "Mixed emotions"

	return emotion

#Detect & print the emotion
emotion = detect_emotion(text)
print("Detected Emotion:", emotion)

#I am so Happy! the weather is beautiful, and everything is going well. I feel very positive and motivated!
#Life is sad and I want to break it into cards